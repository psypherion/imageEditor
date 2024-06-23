############################################ DIP PCA-1 using CV module ############################################
import cv2
import os

DIR_NAME = "edited"
if DIR_NAME not in os.listdir('.'):
    os.mkdir('edited')
    
# Function to show image dimensions
def show_image_dimensions(image):
    dimensions = image.shape
    print(f"Image Dimensions: {dimensions[0]} x {dimensions[1]} (Height x Width)")

# Function to crop image by height and width
def crop_image(image):
    print("Enter the crop dimensions in the format: height,width (e.g., 300,300)")
    crop_dims = input("Crop Dimensions: ")
    crop_height, crop_width = map(int, crop_dims.split(','))
    
    # Get image dimensions
    img_height, img_width = image.shape[:2]
    
    # Calculate the center of the image
    center_y, center_x = img_height // 2, img_width // 2
    
    # Calculate the crop box
    y1 = max(center_y - crop_height // 2, 0)
    y2 = min(center_y + crop_height // 2, img_height)
    x1 = max(center_x - crop_width // 2, 0)
    x2 = min(center_x + crop_width // 2, img_width)
    
    cropped_image = image[y1:y2, x1:x2]
    return cropped_image

# Function to rotate image
def rotate_image(image):
    angle = float(input("Enter the angle to rotate the image (e.g., 45): "))
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

# Function to resize image
def resize_image(image):
    print("Enter the new size in the format: width,height (e.g., 200,200)")
    new_size = input("New Size: ")
    width, height = map(int, new_size.split(','))
    resized_image = cv2.resize(image, (width, height))
    return resized_image

# Open an image file
image_path = "yuv.png"
image = cv2.imread(image_path)

# Show image dimensions
show_image_dimensions(image)

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Ask user if they want to crop the image
if input("Do you want to crop the image? (yes/no): ").strip().lower() == 'yes':
    cropped_image = crop_image(image)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.waitKey(0)

# Ask user if they want to rotate the image
if input("Do you want to rotate the image? (yes/no): ").strip().lower() == 'yes':
    rotated_image = rotate_image(image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)

# Ask user if they want to resize the image
if input("Do you want to resize the image? (yes/no): ").strip().lower() == 'yes':
    resized_image = resize_image(image)
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)

if input("Do You want to save all the images ? (yes/no): ").strip().lower() == 'yes':
    # Save the modified images if any modifications were made
    cv2.waitKey(0)  # Wait for any key press to close all windows
    cv2.destroyAllWindows()  # Close all windows
    cv2.imwrite(f"{DIR_NAME}/cropped_image.jpg", cropped_image) if 'cropped_image' in locals() else None
    cv2.imwrite(f"{DIR_NAME}/rotated_image.jpg", rotated_image) if 'rotated_image' in locals() else None
    cv2.imwrite(f"{DIR_NAME}/resized_image.jpg", resized_image) if 'resized_image' in locals() else None
    



