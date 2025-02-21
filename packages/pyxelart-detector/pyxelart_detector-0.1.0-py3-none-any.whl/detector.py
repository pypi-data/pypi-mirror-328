from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from scipy.fft import fft2, fftshift, ifft2, ifftshift
from skimage import exposure, img_as_float

@dataclass
class CrossKernelOptions:
    line_width_ratio: float = 0.065
    outside_penalty: float = -3.0
    bar_reward: float = 20.0
    center_reward: float = 0.15
    pixel_art_classify_threshold: float = 0.06

EPSILON: float = 1e-7

def do_fft(image: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Perform a two-dimensional Fast Fourier Transform (FFT) on the given image,
    applying the necessary shift operations.

    Parameters:
        image (npt.NDArray[np.float64]): The input image array.

    Returns:
        npt.NDArray[np.float64]: The shifted FFT of the image.
    """
    ishift: npt.NDArray[np.float64] = ifftshift(image)
    fft_img: npt.NDArray[np.float64] = fft2(ishift)
    shift: npt.NDArray[np.float64] = fftshift(fft_img)
    return shift

def crop(image: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Crop the input image to a centered square with an odd side length.

    Parameters:
        image (npt.NDArray[np.float64]): The input image array.

    Returns:
        npt.NDArray[np.float64]: The cropped square image.
    """
    height, width = image.shape
    side = min(height, width)
    if side % 2 == 0:
        side -= 1
    row_start = (height - side) // 2
    col_start = (width - side) // 2

    return image[row_start:row_start + side, col_start:col_start + side]

def generate_cross_kernel(kernel_size: int, options: CrossKernelOptions | None = None) -> npt.NDArray[np.float64]:
    """
    Generate a cross-shaped kernel used for pixel art classification based on the specified options.

    Parameters:
        kernel_size (int): The size of the square kernel.
        options (CrossKernelOptions | None): Configuration options for the kernel generation.
                                               If None, default options are used.

    Returns:
        npt.NDArray[np.float64]: The generated cross kernel.
    """
    USE_THICKNESS_DROPOFF = True
    if options is None:
        options = CrossKernelOptions()
    line_width_ratio, outside_penalty, bar_reward, center_reward = options.line_width_ratio, options.outside_penalty, options.bar_reward, options.center_reward

    K = kernel_size
    # Determine the thickness in pixels (at least 1)
    thickness = max(1, int(line_width_ratio * K) | 1)

    # Determine the center (using float arithmetic for distances)
    center = K // 2

    # Create coordinate grids
    indices = np.indices((K, K))
    Y: npt.NDArray[np.intp] = indices[0]
    X: npt.NDArray[np.intp] = indices[1]

    # Define masks for the vertical and horizontal bars
    mask_horizontal_bar = np.abs(Y - center) <= (thickness // 2)
    mask_vertical_bar   = np.abs(X - center) <= (thickness // 2)

    # TODO This was an idea. Did not work out, but I'll leave it here in case I ever want to test it again
    if USE_THICKNESS_DROPOFF:
        # For pixels on a bar, the reward decays linearly along the "thickness" of the bar
        # I find it hard to phrase that. Basically, looking at the next portion of code:
        # The bars linearly drop off in both dimensions.
        thickness_dropoff_indices = np.indices((thickness, K))[0]
        unpadded: npt.NDArray[np.float64] = 1 - np.abs(thickness_dropoff_indices - (thickness // 2)) / (thickness / 2.0)
        reward_h_thickness_dropoff = np.pad(
            unpadded,
            (((K - thickness) // 2,) * 2, (0,0))
        )
        reward_v_thickness_dropoff = reward_h_thickness_dropoff.T
    else:
        reward_v_thickness_dropoff = 1.0
        reward_h_thickness_dropoff = 1.0

    # For pixels on a bar, the reward also decays linearly with the distance from center.
    # Normalize the vertical distance by half the kernel size.
    reward_v = np.where(mask_vertical_bar, (1 - np.abs(Y - center) / (K / 2.0)) * reward_v_thickness_dropoff, 0)
    reward_h = np.where(mask_horizontal_bar, (1 - np.abs(X - center) / (K / 2.0)) * reward_h_thickness_dropoff, 0)

    reward_v *= bar_reward
    reward_h *= bar_reward

    # Create a kernel with only penalties
    reward = np.ones((K, K)) * outside_penalty
    # zero out the space for the bars
    cross_mask = mask_vertical_bar | mask_horizontal_bar
    reward[cross_mask] = 0.0

    # Combine the rewards.
    # In the bar regions the reward is just that bar's reward.
    reward += reward_v
    reward += reward_h

    # In the center, where both bars overlap, the reward should be a little less,
    # as generally most images have a dot here.
    overlap_mask = mask_vertical_bar & mask_horizontal_bar
    reward[overlap_mask] = center_reward

    return reward

def calculate_classifier(kernel: npt.NDArray[np.float64], image: npt.NDArray[np.float64]) -> float:
    """
    Calculate a classifier score by applying the kernel to the image.

    Parameters:
        kernel (npt.NDArray[np.float64]): The kernel used for weighting the image.
        image (npt.NDArray[np.float64]): The image to classify.

    Returns:
        float: The computed classification score.
    """
    return (kernel * image).sum() / (kernel.size)

def cross_kernel_check(image: npt.NDArray[np.float64], cross_kernel_options: CrossKernelOptions | None = None) -> tuple[bool, list[tuple[str, npt.NDArray[np.float64]]]]:
    """
    Check if the provided thresholded image matches the cross kernel criteria for pixel art.

    Parameters:
        image (npt.NDArray[np.float64]): The thresholded image to check.
        cross_kernel_options (CrossKernelOptions | None): Optional configuration for the cross kernel.
                                                           Defaults to standard options if None.

    Returns:
        tuple:
            bool: True if the image is classified as pixel art, False otherwise.
            list[tuple[str, npt.NDArray[np.float64]]]: Debug data containing the kernel, the processed image,
                                                       and the combined kernel match result.
    """
    kernel_size = image.shape[0]

    kernel = generate_cross_kernel(
        kernel_size,
        options=cross_kernel_options
    )

    if cross_kernel_options is None:
        cross_kernel_options = CrossKernelOptions()

    pixel_art_classifier = calculate_classifier(kernel, image)
    return pixel_art_classifier > cross_kernel_options.pixel_art_classify_threshold, [("kernel", kernel), ("final X", image), ("kernel match", 0.2 * kernel + 0.8 * image)]

def internal_is_pixel_art(image: npt.NDArray[np.float64], debug_all_steps: bool) -> tuple[bool, list[tuple[str, npt.NDArray[np.float64]]]]:
    """
    Determine if the provided image is pixel art by applying FFT-based transformations and a kernel check.

    Parameters:
        image (npt.NDArray[np.float64]): The preprocessed image.
        debug_all_steps (bool): If True, collect and return intermediate processing results for debugging.

    Returns:
        tuple:
            bool: True if the image is identified as pixel art, False otherwise.
            list[tuple[str, npt.NDArray[np.float64]]]: A list of intermediate images and debug data.
    """
    side_len = image.shape[0]
    in_betweens: list[tuple[str, npt.NDArray[np.float64]]] = []

    fft_image: npt.NDArray[np.float64] = np.log(np.maximum(EPSILON, abs(do_fft(image))))
    clipped: npt.NDArray[np.float64] = np.clip(fft_image, 0.0, 1.0)
    if debug_all_steps:
        in_betweens.append(("FFT", clipped))

    inverted: npt.NDArray[np.float64] = abs(clipped - 1.0)
    if debug_all_steps:
        in_betweens.append(("inverted", inverted))

    rescaled: npt.NDArray[np.float64] = exposure.rescale_intensity(inverted, in_range=(0, inverted.max()), out_range=(0, 1))
    if debug_all_steps:
        in_betweens.append(("rescaled", rescaled))

    second_fft: npt.NDArray[np.float64] = np.log(abs(do_fft(rescaled)))
    if debug_all_steps:
        in_betweens.append(("2nd FFT", second_fft))

    rescaled_second: npt.NDArray[np.float64] = exposure.rescale_intensity(second_fft, in_range=(second_fft.min(), second_fft.max()), out_range=(0.0, 1.0))
    if debug_all_steps:
        in_betweens.append(("2nd rescaled", rescaled_second))

    threshold = 0.76
    thresholded = rescaled_second > threshold
    crop_factor = 0.05 # crop factor
    left = max(int(side_len//2 - np.floor(crop_factor * side_len)), 1)
    right = max(int(side_len//2 + np.ceil(crop_factor * side_len)), 1)
    cropped_threshold = thresholded[left:right,left:right]

    pixel_art, in_betweens_kernel_check = cross_kernel_check(cropped_threshold)

    return pixel_art, in_betweens + in_betweens_kernel_check

def get_prepared_image(filepath: Path) -> npt.NDArray[np.float64]:
    """
    Load an image from the specified file path and preprocess it by converting to float
    (if necessary), transforming to grayscale, and cropping to a centered square
    with an odd side length.

    Parameters:
        filepath (Path): The path to the image file.

    Returns:
        npt.NDArray[np.float64]: The preprocessed image ready for analysis.
    """
    # Read the image
    im_raw = plt.imread(filepath)
    return get_prepared_image_numpy(im_raw)

def get_prepared_image_numpy(image: np.NDArray[np.float64]) -> npt.NDArray[np.float64]:
    """
    Preprocess a given image (as a numpy array) by converting to float (if necessary),
    transforming to grayscale, and cropping to a centered square with an odd side length.

    Parameters:
        image (npt.NDArray[np.float64]): The image as a numpy array.

    Returns:
        npt.NDArray[np.float64]: The preprocessed image ready for analysis.
    """
    # Make sure we have values in the range of [0-1]
    im_float: npt.NDArray[np.float64] = img_as_float(image)
    # Grayscale
    im_gray: npt.NDArray[np.float64] = np.mean(im_float[:,:,:3], axis=2)
    # Crop it, so it is square with an odd length
    im_crop: npt.NDArray[np.float64] = crop(im_gray)
    return im_crop


def is_pixel_art(filepath: Path) -> bool:
    """
    Determine if an image (loaded from the specified file path) qualifies as pixel art.

    Parameters:
        filepath (Path): The path to the image file.

    Returns:
        bool: True if the image is classified as pixel art, False otherwise.
    """
    pixel_art, _images = is_pixel_art_debug(filepath)
    return pixel_art

def is_pixel_art_numpy(image: npt.NDArray[np.float64]):
    """
    Determine if an image (as a numpy array) qualifies as pixel art.

    Parameters:
        image (npt.NDArray[np.float64]): The image as a numpy array.

    Returns:
        bool: True if the image is classified as pixel art, False otherwise.
    """
    prepared_image = get_prepared_image_numpy(image)
    pixel_art, _in_betweens = internal_is_pixel_art(prepared_image, False)
    return pixel_art

def is_pixel_art_debug(filepath: Path, debug_all_steps: bool = False) -> tuple[bool, list[tuple[str, npt.NDArray[np.float64]]]]:
    """
    Determine if an image is pixel art, providing additional debug information for each processing step.

    Parameters:
        filepath (Path): The path to the image file.
        debug_all_steps (bool, optional): If True, returns intermediate processing results for debugging.
                                          Defaults to False.

    Returns:
        tuple:
            bool: True if the image is classified as pixel art, False otherwise.
            list[tuple[str, npt.NDArray[np.float64]]]: Debug data including the original image and intermediate results.
    """
    prepared_img = get_prepared_image(filepath)
    pixel_art, in_betweens = internal_is_pixel_art(prepared_img, debug_all_steps)
    return pixel_art, [("Original", prepared_img)] + in_betweens
