############################################ DIP PCA-1 using Pillow module ############################################

from PIL import Image
import os

# Directory name to save edited images
DIR_NAME = "modified"
if DIR_NAME not in os.listdir('.'):
    os.mkdir(DIR_NAME)

image_path = "test.jpg" # Path of the image

# Function to show image dimensions
def show_image_dimensions(image):
    dimensions = image.size  
    print(f"Image Dimensions: {dimensions[1]} x {dimensions[0]} (Height x Width)")

# Function to crop image by height and width
def crop_image(image):
    print("Enter the crop dimensions in the format: height,width (e.g., 300,300)")
    crop_dims = input("Crop Dimensions: ")
    crop_height, crop_width = map(int, crop_dims.split(','))
    # Get image dimensions
    img_width, img_height = image.size
    # Calculate the center of the image
    center_y, center_x = img_height // 2, img_width // 2
    # Calculate the crop box
    y1 = max(center_y - crop_height // 2, 0)
    y2 = min(center_y + crop_height // 2, img_height)
    x1 = max(center_x - crop_width // 2, 0)
    x2 = min(center_x + crop_width // 2, img_width)

    cropped_image = image.crop((x1, y1, x2, y2))
    return cropped_image

# Function to rotate image
def rotate_image(image):
    angle = float(input("Enter the angle to rotate the image (e.g., 45): "))
    rotated_image = image.rotate(angle, expand=True)
    return rotated_image

# Function to resize image
def resize_image(image):
    print("Enter the new size in the format: width,height (e.g., 200,200)")
    new_size = input("New Size: ")
    width, height = map(int, new_size.split(','))
    resized_image = image.resize((width, height))
    return resized_image

# Function to ask for user input with a default option
def get_user_input(prompt, default='Y'):
    user_input = input(f"{prompt} (Y/n): ").strip().lower()
    return user_input in ['y', 'yes', '']

# Open an image file
image = Image.open(image_path)

# Show image dimensions
show_image_dimensions(image)

# Display the original image
image.show(title='Original Image')

# Ask user if they want to crop the image
crop_option = get_user_input("Do you want to crop the image")
if crop_option:
    cropped_image = crop_image(image)
    cropped_image.show(title='Cropped Image')

# Ask user if they want to rotate the image
rotate_option = get_user_input("Do you want to rotate the image")
if rotate_option:
    rotated_image = rotate_image(image)
    rotated_image.show(title='Rotated Image')

# Ask user if they want to resize the image
resize_option = get_user_input("Do you want to resize the image")
if resize_option:
    resized_image = resize_image(image)
    resized_image.show(title='Resized Image')


# Ask user if they want to save the images
save_option = get_user_input("Do you want to save all the images")
if save_option:
    input("Press Enter to save and close all image windows.")
    # Save the modified images if any modifications were made
    cropped_image.save(f"{DIR_NAME}/cropped_image.jpg") if 'cropped_image' in locals() else None
    rotated_image.save(f"{DIR_NAME}/rotated_image.jpg") if 'rotated_image' in locals() else None
    resized_image.save(f"{DIR_NAME}/resized_image.jpg") if 'resized_image' in locals() else None
