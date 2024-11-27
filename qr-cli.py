#!/usr/bin/env python3

import argparse
import requests
from PIL import Image
from io import BytesIO
from pyzbar.pyzbar import decode

def extract_qr_data(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = BytesIO(response.content)

        img = Image.open(image_data)

        qr_data = decode(img)
        if qr_data:
            return qr_data[0].data.decode("utf-8")
        else:
            return "No QR code found in the image"

    except requests.exceptions.RequestException as e:
        return f"Failed to fetch image: {e}"
    except Exception as e:
        return f"An error occured: {e}"

def main():
    parser = argparse.ArgumentParser(description="QR Code Reader from Image URL")
    parser.add_argument("url", help="URL of the image containing the QR code")
    args = parser.parse_args()

    qr_data = extract_qr_data(args.url)
    print("Extracted QR Code Data:", qr_data)

if __name__ == "__main__":
    main()
    
