# QR Reader CLI Tool

A simple command-line tool to decode QR codes from image URLs and extract the embedded data.

## Features

- Fetches images from a provided URL.
- Decodes QR codes from the image.
- Outputs the extracted data directly to the console.

## Requirements

- Python 3.6 or later
- Internet connection to fetch images from the provided URL.

## Dependencies

The tool relies on the following Python libraries:

- `requests`: For fetching the image from the URL.
- `Pillow`: For handling image data.
- `pyzbar`: For decoding QR codes.

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have Python 3 installed on your system.
3. Install the required dependencies using `pip`:

   ```bash
   pip install requests pillow pyzbar
   ```

4. Make the script executable (optional):

  ```bash
  chmod +x qr-reader.py
  ```

## Usage

Run the script by providing the URL of an image containing a QR code:

`./qr-reader.py <image-url>`

Alternatively, run it directly with Python:

`python qr-reader.py <image-url>`

### Example

./qr-reader.py https://example.com/images/image-with-qr.png

Output:

Extracted QR Code Data: https://example.com

## Troubleshooting

### ImportError: Unable to find zbar shared library

If you encounter this error, ensure the `zbar` library is installed on your system:

- Ubuntu/Debian:

  `sudo apt install libzbar0`

- Fedora:

  `sudo dnf install zbar`

- Arch Linux:

  `sudo pacman -S zbar`

- macOS (Homebrew):

  `brew install zbar`


### Other Issues

Ensure all Python dependencies are installed. You can reinstall them if necessary:
`pip install --force-reinstall requests pillow pyzbar`


## License

This project is licensed under the MIT License. See the LICENSE file for details.

