from PIL import Image
import numpy as np
import os

# 1. Load the image
def load_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
        return None

# 2. Encrypt image by swapping the red and blue channels or adding a shift
def encrypt_image(image):
    pixels = np.array(image)
    
    # Option 1: Swap red and blue channels
    encrypted_pixels = pixels.copy()
    encrypted_pixels[..., [0, 2]] = encrypted_pixels[..., [2, 0]]  # Swap red and blue
    
    # Option 2: Apply a mathematical operation (shift pixel values)
    encrypted_pixels = (encrypted_pixels + 50) % 256  # Adding shift for encryption
    
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    return encrypted_image

# 3. Decrypt image by reversing the operations
def decrypt_image(encrypted_image):
    pixels = np.array(encrypted_image)
    
    # Reverse Option 1: Swap red and blue channels back
    decrypted_pixels = pixels.copy()
    decrypted_pixels[..., [0, 2]] = decrypted_pixels[..., [2, 0]]  # Swap back red and blue
    
    # Reverse Option 2: Subtract the shift
    decrypted_pixels = (decrypted_pixels - 50) % 256  # Reverse the shift
    
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    return decrypted_image

# Main logic for encryption and decryption
def process_image():
    # Get image path from user
    image_path = input("Enter the full path to the image: ")
    
    # Check if the file exists
    if not os.path.exists(image_path):
        print("The file does not exist. Please try again.")
        return
    
    # Load the original image
    original_image = load_image(image_path)
    
    if original_image is None:
        return  # Exit if the image could not be loaded
    
    # Encrypt the image
    encrypted_image = encrypt_image(original_image)
    encrypted_image.save("encrypted_image.png")
    print("Encrypted image saved as 'encrypted_image.png'")
    
    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image)
    decrypted_image.save("decrypted_image.png")
    print("Decrypted image saved as 'decrypted_image.png'")

# Example usage
process_image()
