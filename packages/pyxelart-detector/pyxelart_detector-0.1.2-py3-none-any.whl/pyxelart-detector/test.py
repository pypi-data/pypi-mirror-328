#!/usr/bin/env python3
"""
Test script for the pyxelart-detector library.

This script is intended for testing and demonstration purposes.
Developers should use the functions `is_pixel_art()` and `is_pixel_art_numpy()`
from the `pyxelart_detector` package.
Usage examples:
  test.py <directory>
  test.py <file1> <file2> ... [--interactive] [--always-plot]
"""

import sys
from pathlib import Path
import argparse
from dataclasses import dataclass

import numpy as np
import numpy.typing as npt
from termcolor import colored

from .pyxelart_detector import (
    CrossKernelOptions,
    is_pixel_art_debug,
    is_pixel_art,
    calculate_classifier,
    cross_kernel_check,
)

# =============================================================================
# Argument parsing and file loading
# =============================================================================
def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Detect pixel art images from a list of files or a directory."
    )
    _ = parser.add_argument(
        "inputs",
        nargs="+",
        help="Either a directory of images or a list of image files.",
    )
    _ = parser.add_argument(
        "--interactive",
        action="store_true",
        help="Run in interactive/debug mode (slider interface).",
    )
    _ = parser.add_argument(
        "--always-plot",
        action="store_true",
        help='Always display plots, even if classification is correct (ground truth is if the filename starts with "pixel".',
    )
    return parser.parse_args()


def load_filepaths(inputs: list[str]) -> list[Path]:
    """
    Given a list of input strings, interpret as either a directory (if one item and a directory)
    or as a list of file paths.
    """
    paths: list[Path] = []
    first_path = Path(inputs[0])
    if first_path.is_dir() and len(inputs) == 1:
        for filepath in first_path.iterdir():
            if filepath.is_file():
                paths.append(filepath)
    else:
        for filearg in inputs:
            filepath = Path(filearg)
            if not filepath.is_file():
                print(f"Warning: {filepath} is not a file. Skipping.")
            else:
                paths.append(filepath)
    if not paths:
        sys.exit("No valid image files found.")
    return paths


# =============================================================================
# Plotting functions
# =============================================================================
def plot(
    interactive: bool,
    to_be_plotted: list[tuple[str, list[tuple[str, npt.NDArray[np.float64]]]]]
) -> None:
    """
    Set up and run interactive mode with sliders to adjust kernel options.
    """

    from matplotlib.axes import Axes
    from matplotlib.image import AxesImage
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider
    from mpl_interactions import zoom_factory

    # =============================================================================
    # Data classes for plot management
    # =============================================================================
    @dataclass
    class PlotItem:
        """Data class to hold the subplot axes, image artists, and a reference frame."""
        ax_original: Axes
        im_original: AxesImage
        ax_kernel: Axes
        im_kernel: AxesImage
        ax_final: Axes
        im_final: AxesImage
        ax_overlay: Axes
        im_overlay: AxesImage
        saved_frame: npt.NDArray[np.float64]

    kernel_options = CrossKernelOptions()

    fig = plt.figure(figsize=(30, 30))
    plt.set_cmap("gray")
    plt.ioff()

    num_plots = len(to_be_plotted)
    cols = 4  # Number of subplots per image: Original, Kernel, Final X, Kernel Match
    plot_items: list[PlotItem] = []

    # Create subplots for each image that will be updated interactively.
    for i, (name, debug_steps) in enumerate(to_be_plotted):
        # Expected indices from debug_steps:
        # 0: "Original", -3: "kernel", -2: "final X", -1: "kernel match"
        _, orig_frame = debug_steps[0]
        _, kernel_img = debug_steps[-3]
        _, final_img = debug_steps[-2]
        _, overlay_img = debug_steps[-1]

        ax_orig = fig.add_subplot(num_plots, cols, i * cols + 1)
        im_orig = ax_orig.imshow(orig_frame)
        ax_orig.axis("off")
        ax_orig.set_title("Original")

        ax_kernel = fig.add_subplot(num_plots, cols, i * cols + 2)
        im_kernel = ax_kernel.imshow(kernel_img)
        ax_kernel.axis("off")
        ax_kernel.set_title("Kernel")

        ax_final = fig.add_subplot(num_plots, cols, i * cols + 3)
        im_final = ax_final.imshow(final_img)
        ax_final.axis("off")
        ax_final.set_title("Final X")

        ax_overlay = fig.add_subplot(num_plots, cols, i * cols + 4)
        im_overlay = ax_overlay.imshow(overlay_img)
        ax_overlay.axis("off")
        ax_overlay.set_title(f"Classifier: {calculate_classifier(kernel_img, final_img):.3f}")

        plot_items.append(
            PlotItem(
                ax_original=ax_orig,
                im_original=im_orig,
                ax_kernel=ax_kernel,
                im_kernel=im_kernel,
                ax_final=ax_final,
                im_final=im_final,
                ax_overlay=ax_overlay,
                im_overlay=im_overlay,
                saved_frame=final_img.copy(),
            )
        )

    if interactive:
        # Create sliders for adjustable parameters.
        slider_axes = {
            "thickness": fig.add_axes((0.01, 0.25, 0.0225, 0.63)),
            "penalty": fig.add_axes((0.05, 0.25, 0.0225, 0.63)),
            "bar_reward": fig.add_axes((0.09, 0.25, 0.0225, 0.63)),
            "threshold": fig.add_axes((0.13, 0.25, 0.0225, 0.63)),
            "center": fig.add_axes((0.17, 0.25, 0.0225, 0.63)),
        }

        sliders = {
            "thickness": Slider(
                ax=slider_axes["thickness"],
                label="Thickness",
                valmin=0.0,
                valmax=1.0,
                valinit=kernel_options.line_width_ratio,
                orientation="vertical",
            ),
            "penalty": Slider(
                ax=slider_axes["penalty"],
                label="Penalty",
                valmin=0.1,
                valmax=5.0,
                valinit=-kernel_options.outside_penalty,
                orientation="vertical",
            ),
            "bar_reward": Slider(
                ax=slider_axes["bar_reward"],
                label="Bar Reward",
                valmin=5.0,
                valmax=60.0,
                valinit=kernel_options.bar_reward,
                orientation="vertical",
            ),
            "threshold": Slider(
                ax=slider_axes["threshold"],
                label="Threshold",
                valmin=-1.0,
                valmax=1.0,
                valinit=kernel_options.pixel_art_classify_threshold,
                orientation="vertical",
            ),
            "center": Slider(
                ax=slider_axes["center"],
                label="Center",
                valmin=-1.0,
                valmax=1.0,
                valinit=kernel_options.center_reward,
                orientation="vertical",
            ),
        }

        def update(_val):
            # Update kernel options from slider values.
            kernel_options.line_width_ratio = sliders["thickness"].val
            kernel_options.pixel_art_classify_threshold = sliders["threshold"].val
            kernel_options.bar_reward = sliders["bar_reward"].val
            kernel_options.outside_penalty = -sliders["penalty"].val
            kernel_options.center_reward = sliders["center"].val

            # Update each subplot based on the new options.
            for item in plot_items:
                # Recompute cross kernel check on the saved frame.
                is_pa, new_debug = cross_kernel_check(item.saved_frame.copy(), cross_kernel_options=kernel_options)
                # Expected indices: -3: "kernel", -2: "final X", -1: "kernel match"
                _, new_kernel = new_debug[-3]
                _, new_final = new_debug[-2]
                _, new_overlay = new_debug[-1]

                item.ax_original.set_title(f"Original\n{is_pa}")
                classifier_value = calculate_classifier(new_kernel, new_final)
                item.ax_overlay.set_title(f"Classifier: {classifier_value:.3f}")

                item.im_kernel.set_data(new_kernel)
                item.im_final.set_data(new_final)
                item.im_overlay.set_data(new_overlay.copy())
            fig.canvas.draw_idle()

        for slider in sliders.values():
            slider.on_changed(update)

    plt.show()


# =============================================================================
# Main processing function
# =============================================================================
def main() -> None:
    args = parse_arguments()
    interactive: bool = args.interactive  # pyright: ignore
    always_plot: bool = args.always_plot

    should_plot: bool = interactive or always_plot

    filepaths: list[Path] = load_filepaths(args.inputs)
    results: list[tuple[str, bool, list[tuple[str, npt.NDArray[np.float64]]]]] = []

    # Process each file with the detector.
    for filepath in filepaths:
        if should_plot:
            pixel_art, debug_steps = is_pixel_art_debug(filepath)
            results.append((filepath.name, pixel_art, debug_steps))
        else:
            pixel_art = is_pixel_art(filepath)
            print(filepath, pixel_art, sep=':')

    if should_plot:
        # Prepare list of images to plot: if classification is incorrect or if always_plot is True.
        to_be_plotted: list[tuple[str, list[tuple[str, npt.NDArray[np.float64]]]]] = []
        for name, pixel_art, debug_steps in results:
            should_be_pixel_art = name.startswith("pixel")
            correctly_classified = (pixel_art == should_be_pixel_art)
            print(colored(f"{name}: {pixel_art}", "green" if correctly_classified else "red"))
            if (not correctly_classified or always_plot):
                to_be_plotted.append((name, debug_steps))

        plot(interactive, to_be_plotted)

if __name__ == "__main__":
    main()
