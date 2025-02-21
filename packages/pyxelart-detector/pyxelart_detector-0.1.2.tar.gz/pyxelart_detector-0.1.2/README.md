# PyxelArt Detector

PyxelArt Detector is a Python library for analyzing images to determine if they qualify as pixel art.

```bash
$ python3 -m pyxelart_detector ./example.png
True
```

## Features

- **Accurate Detection**: Uses FFT-based transformations and a tailored cross-kernel approach to identify pixel art. Reach out via the [issues](https://github.com/dann-merlin/pyxelart-detector), if you think the library misclassified an image.
- **Simple API**: I don't like "complicated", so here you go:
  - `is_pixel_art(filepath: Path) -> bool`
  - `is_pixel_art_numpy(image: np.ndarray) -> bool`

## Installation

Install via uv/pip:

```bash
uv add pyxelart-detector
# or
pip install pyxelart-detector
```

## Usage

After installation, import and use the library in your projects as follows:

```python
from pyxelart_detector import is_pixel_art, is_pixel_art_numpy

# Example using the file-based API
result = is_pixel_art("path/to/your/image.png")
if result:
    print("This is pixel art!")
else:
    print("Not pixel art.")

# Example using the NumPy-based API
import matplotlib.pyplot as plt
image = plt.imread("path/to/your/image.png")
if is_pixel_art_numpy(image):
    print("This is pixel art!")
else:
    print("Not pixel art.")
```

## Contributing

Contributions are welcome! If you have ideas or improvements, please open an issue or submit a pull request on [GitHub](https://github.com/dann-merlin/pyxelart-detector).

## Acknowledgments

This library is built on excellent open-source tools,
including [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/),
and others.
