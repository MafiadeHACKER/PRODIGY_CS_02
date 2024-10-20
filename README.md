# PRODIGY_CS_02

# Image Encryption Tool - Pixel Manipulation

# Description
This Python program is a simple image encryption tool that allows users to encrypt and decrypt images using pixel manipulation techniques. It performs operations such as swapping pixel values (e.g., red and blue channels) or applying a basic mathematical operation (e.g., adding a constant value) to encrypt the image. The program also provides the ability to reverse these operations to decrypt the image back to its original form.

# Features
# Image Encryption:
Swaps the red and blue color channels of the image.
Optionally applies a mathematical shift to the pixel values.
# Image Decryption:
Reverses the encryption by swapping the channels back or reversing the shift.

# Requirements
Python 3.x
Pillow (PIL)
You can install Pillow using pip:
    pip install pillow

NumPy
You can install NumPy using pip:
    pip install numpy

# Usage
Clone or download this repository.
Ensure you have an image file ready for encryption.
Run the script and provide the image path when prompted.

# Steps:
The program will load the image from the provided path.
The image will then be encrypted and saved as encrypted_image.png.
After encryption, the image will be decrypted and saved as decrypted_image.png.

# Example:
python image_encryption.py
When prompted:
Enter the path to the image file: /path/to/image.jpg

# How It Works
Load the Image:
The image is loaded from the user-specified path using the PIL library.
Encrypt the Image:
The red and blue color channels of the image are swapped.
Alternatively, a mathematical operation (e.g., adding 50 to each pixel value) is applied to encrypt the image.
Decrypt the Image:
The swapping of color channels is reversed.
The mathematical shift applied during encryption is subtracted to recover the original image.

# Output
encrypted_image.png: The encrypted version of the input image.
decrypted_image.png: The decrypted image, restored to its original form.