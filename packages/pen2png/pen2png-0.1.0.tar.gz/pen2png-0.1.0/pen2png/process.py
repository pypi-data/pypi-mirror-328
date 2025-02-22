import cv2
import numpy as np
from PIL import Image, UnidentifiedImageError
import pillow_heif
import os


def load_image(input_path):
    """Loads an image, converting HEIC to a format OpenCV can process."""
    try:
        if input_path.lower().endswith(".heic"):
            heif_image = pillow_heif.open_heif(input_path)
            image = Image.frombytes(heif_image.mode, heif_image.size, heif_image.data)
            image = image.convert("L")
        else:
            image = Image.open(input_path).convert("L")

        return np.array(image)

    except UnidentifiedImageError:
        raise ValueError(
            f"Error: Unable to load image '{input_path}'. Unsupported format or corrupted file."
        )


def process_image(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Error: Input file '{input_path}' not found.")

    # load image
    image = load_image(input_path)

    # gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # otsu's thresholding
    _, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # invert colors so ink is black and paper is white
    binary = cv2.bitwise_not(binary)

    # convert to rgba
    h, w = binary.shape
    result = np.zeros((h, w, 4), dtype=np.uint8)
    result[:, :, 0:3] = 0  # Set all RGB channels to black
    result[:, :, 3] = binary  # Alpha channel from binary image

    # save as transparent PNG
    try:
        final_image = Image.fromarray(result)
        final_image.save(output_path, format="PNG")
        print(f"Processed image saved to {output_path}")
    except Exception as e:
        raise ValueError(f"Error: Unable to save image '{output_path}'. {e}")
