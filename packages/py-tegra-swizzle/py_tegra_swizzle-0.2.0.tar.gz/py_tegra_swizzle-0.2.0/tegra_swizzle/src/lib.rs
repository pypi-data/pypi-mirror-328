//! # tegra_swizzle
//! tegra_swizzle is a CPU implementation of the
//! Tegra X1 block linear memory tiling for texture surfaces.
//!
//! ## Getting Started
//! Tiled texture data in binary files is often stored in a single buffer containing all arrays and mipmaps.
//! This memory layout can be untiled all at once using [surface::deswizzle_surface].
//!
//! # Block Linear Memory Tiling
//! The [surface::swizzle_surface] and [surface::deswizzle_surface] functions
//! implement safe and efficient tiling and untiling for the Tegra X1's block linear format.
//!
//! Block linear arranges bytes of a texture surface into a 2D grid of blocks
//! where blocks are arranged linearly in row-major order.
//! The tiled surface size is padded to integral dimensions in blocks, so
//! tiled surfaces may be larger than the corresponding data in row-major order.
//!
//! Groups of 512 bytes form GOBs ("group of bytes") where each GOB is 64x8 bytes.
//! The `block_height` parameter determines how many GOBs stack vertically to form a block.
#![no_std]
extern crate alloc;

#[cfg(feature = "std")]
extern crate std;

mod arrays;
mod blockdepth;
mod blockheight;

pub mod surface;
pub mod swizzle;

#[cfg(feature = "ffi")]
pub mod ffi;

pub use blockheight::*;

const GOB_WIDTH_IN_BYTES: u32 = 64;
const GOB_HEIGHT_IN_BYTES: u32 = 8;
const GOB_SIZE_IN_BYTES: u32 = GOB_WIDTH_IN_BYTES * GOB_HEIGHT_IN_BYTES;

// Block height can only have certain values based on the Tegra TRM page 1189 table 79.

/// The height of each block in GOBs where each GOB is 8 bytes tall.
///
/// Texture file formats differ in how they encode the block height parameter.
/// Some formats may encode block height using log2, so a block height of 8 would be encoded as 3.
/// For formats that do not explicitly store block height, see [block_height_mip0].
#[derive(Debug, PartialEq, Eq, Clone, Copy)]
#[cfg_attr(feature = "arbitrary", derive(arbitrary::Arbitrary))]
pub enum BlockHeight {
    One = 1,
    Two = 2,
    Four = 4,
    Eight = 8,
    Sixteen = 16,
    ThirtyTwo = 32,
}

/// Errors than can occur while tiling or untiling.
#[derive(Debug, PartialEq, Eq)]
pub enum SwizzleError {
    /// The source data does not contain enough bytes.
    /// See the documentation for functions like [surface::swizzle_surface] and [surface::deswizzle_surface]
    /// for how to calculate the expected size.
    NotEnoughData {
        expected_size: usize,
        actual_size: usize,
    },

    /// The surface dimensions would overflow in size calculations.
    InvalidSurface {
        width: u32,
        height: u32,
        depth: u32,
        bytes_per_pixel: u32,
        mipmap_count: u32,
    },
}

#[cfg(feature = "std")]
impl std::fmt::Display for SwizzleError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            SwizzleError::NotEnoughData {
                expected_size,
                actual_size,
            } => write!(
                f,
                "Expected at least {expected_size} bytes but found {actual_size} bytes"
            ),
            SwizzleError::InvalidSurface {
                width,
                height,
                depth,
                bytes_per_pixel,
                mipmap_count,
            } => write!(f, "Invalid surface dimensions {width}x{height}x{depth} with {bytes_per_pixel} bytes per pixel and {mipmap_count} mipmaps"),
        }
    }
}

#[cfg(feature = "std")]
impl std::error::Error for SwizzleError {}

impl BlockHeight {
    /// Attempts to construct a block height from `value`.
    /// Returns [None] if `value` is not a supported block height.
    /// # Examples
    /**
    ```rust
    use tegra_swizzle::BlockHeight;

    assert_eq!(Some(BlockHeight::Eight), BlockHeight::new(8));
    assert_eq!(None, BlockHeight::new(5));
    ```
    */
    pub fn new(value: u32) -> Option<Self> {
        match value {
            1 => Some(BlockHeight::One),
            2 => Some(BlockHeight::Two),
            4 => Some(BlockHeight::Four),
            8 => Some(BlockHeight::Eight),
            16 => Some(BlockHeight::Sixteen),
            32 => Some(BlockHeight::ThirtyTwo),
            _ => None,
        }
    }
}

const fn height_in_blocks(height: u32, block_height: u32) -> u32 {
    // Each block is block_height many GOBs tall.
    div_round_up(height, block_height * GOB_HEIGHT_IN_BYTES)
}

/// Calculates the division of `x` by `d` but rounds up rather than truncating.
///
/// # Examples
/// Use this function when calculating dimensions for block compressed formats like BC7.
/**
```rust
# use tegra_swizzle::div_round_up;
assert_eq!(2, div_round_up(8, 4));
assert_eq!(3, div_round_up(10, 4));
```
 */
/// Uncompressed formats are equivalent to 1x1 pixel blocks.
/// The call to [div_round_up] can simply be ommitted in these cases.
/**
```rust
# use tegra_swizzle::div_round_up;
let n = 10;
assert_eq!(n, div_round_up(n, 1));
```
 */
#[inline]
pub const fn div_round_up(x: u32, d: u32) -> u32 {
    (x + d - 1) / d
}

const fn width_in_gobs(width: u32, bytes_per_pixel: u32) -> u32 {
    div_round_up(width * bytes_per_pixel, GOB_WIDTH_IN_BYTES)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::swizzle::{deswizzled_mip_size, swizzled_mip_size};

    #[test]
    fn width_in_gobs_block16() {
        assert_eq!(20, width_in_gobs(320 / 4, 16));
    }

    #[test]
    fn deswizzled_mip_sizes() {
        assert_eq!(3145728, deswizzled_mip_size(512, 512, 3, 4));
    }

    #[test]
    fn surface_sizes_block4() {
        assert_eq!(
            1048576,
            swizzled_mip_size(512, 512, 1, BlockHeight::Sixteen, 4)
        );
    }

    #[test]
    fn surface_sizes_3d() {
        assert_eq!(16384, swizzled_mip_size(16, 16, 16, BlockHeight::One, 4));
    }

    #[test]
    fn surface_sizes_block16() {
        assert_eq!(
            163840,
            swizzled_mip_size(320 / 4, 320 / 4, 1, BlockHeight::Sixteen, 16)
        );
        assert_eq!(
            40960,
            swizzled_mip_size(160 / 4, 160 / 4, 1, BlockHeight::Four, 16)
        );
        assert_eq!(
            1024,
            swizzled_mip_size(32 / 4, 32 / 4, 1, BlockHeight::One, 16)
        );
    }
}
