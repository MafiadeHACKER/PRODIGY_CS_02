from PIL import Image, ImageDraw
import numpy as np

# Function to create a blue gradient background (Optional use)
def create_blue_gradient(width, height):
    img = Image.new('RGB', (width, height))
    for y in range(height):
        blue_value = int(255 * (y / height))  # Gradient from top to bottom
        for x in range(width):
            img.putpixel((x, y), (0, 0, blue_value))  # Blue gradient
    return img
 
# Function to draw a circle with a gradient (Optional use) 
def create_circle_with_gradient(img, center, radius): 
    draw = ImageDraw.Draw(img)
    for r in range(radius, 0, -1):
        color_value = int(255 * (r / radius))
        draw.ellipse([center[0] - r, center[1] - r, center[0] + r, center[1] + r], fill=(color_value, color_value, color_value))
    return img

# Function for pixel manipulation (encryption)
def encrypt_image(image, key):
    img_array = np.array(image)
    encrypted_array = (img_array + key) % 256  # Simple encryption by adding a key
    return Image.fromarray(encrypted_array)

# Function for pixel manipulation (decryption)
def decrypt_image(image, key):
    img_array = np.array(image)
    decrypted_array = (img_array - key) % 256  # Reverse operation by subtracting the key
    return Image.fromarray(decrypted_array)

# Function to get user input for image path and operation
def get_user_input():
    image_path = input("Enter the path to the image file (e.g., 'image.png'): ").strip()
    operation = input("Do you want to encrypt or decrypt the image? (Enter 'encrypt' or 'decrypt'): ").strip().lower()
    return image_path, operation

# Main function to execute the task
def main():
    # Get user input for image path and operation
    image_path, operation = get_user_input()
    
    try:
        # Load the image
        image = Image.open(image_path)
        image.show(title="Original Image")

        # Choose encryption key
        encryption_key = int(input("Enter an encryption key (a number between 0 and 255): ").strip())
        
        # Perform the operation based on user choice
        if operation == 'encrypt':
            # Encrypt the image
            encrypted_image = encrypt_image(image, encryption_key)
            encrypted_image.show(title="Encrypted Image")
            # Save encrypted image
            encrypted_image.save("encrypted_image.png")
            print("Image has been encrypted and saved as 'encrypted_image.png'.")
        
        elif operation == 'decrypt':
            # Decrypt the image
            decrypted_image = decrypt_image(image, encryption_key)
            decrypted_image.show(title="Decrypted Image")
            # Save decrypted image
            decrypted_image.save("decrypted_image.png")
            print("Image has been decrypted and saved as 'decrypted_image.png'.")
        
        else:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
    
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
    except ValueError:
        print("Error: Invalid encryption key. Please enter a valid number between 0 and 255.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
