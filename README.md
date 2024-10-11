# PRODIGY_CS_02

# Simple Image Encryption Tool
This Python script allows users to encrypt and decrypt images using pixel manipulation. The script enables users to choose an image file, input an encryption key, and decide whether to encrypt or decrypt the image.

# Features
Encrypt Image: Add a key value to each pixel of the image for encryption.
Decrypt Image: Subtract the key value from each pixel to restore the original image.
User Interaction: Input-based system where users provide the image file path and choose the operation (encryption or decryption).

# Requirements
Python 3.x
Pillow library (for image manipulation)
NumPy library (for pixel-level operations)

# Installation
Install Python: Make sure you have Python 3 installed on your system. If not, you can download it from python.org.

Install Dependencies: Install the required libraries using pip:
    pip install pillow numpy

# Usage
Run the Script: Execute the script in a terminal or Python IDE:
    python image_encryption.py

# Input Prompts:
The script will ask you to provide the path to the image file (e.g., image.png).
Choose whether to "encrypt" or "decrypt" the image by typing encrypt or decrypt.
Input a number between 0 and 255 as the encryption key.

# Output:
The original image will be displayed.
After processing, either the encrypted or decrypted image will be shown.
The processed image will be saved in the same directory with the names:
    encrypted_image.png for encrypted images.
    decrypted_image.png for decrypted images.

# Example
Enter the path to the image file (e.g., 'image.png'): image.png
Do you want to encrypt or decrypt the image? (Enter 'encrypt' or 'decrypt'): encrypt
Enter an encryption key (a number between 0 and 255): 50

After completing the encryption or decryption, the resulting image will be saved in the working directory, and a message will confirm the operation.

# Error Handling
File Not Found: If the provided image path is incorrect, you will get an error message.
Invalid Key: Ensure the encryption key is a number between 0 and 255. Otherwise, a warning will be shown.
Optional (Blue Gradient and Circle with Gradient)
The script contains optional functions to create a blue gradient background and draw a circle with a gradient on an image. These functions can be used if needed but are not critical for the encryption and decryption processes.