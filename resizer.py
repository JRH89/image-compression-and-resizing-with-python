import os
import argparse
from PIL import Image

def resize_image(image_path, output_path, width, height):
    try:
        with Image.open(image_path) as img:
            # Resize the image to the specified dimensions without maintaining aspect ratio
            img = img.resize((width, height), Image.LANCZOS)  # Use LANCZOS for better quality
            img.save(output_path)
            print(f"Resized {image_path} and saved as {output_path}")
    except Exception as e:
        print(f"Error resizing {image_path}: {e}")

def resize_images_in_directory(directory, output_directory, width, height):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                image_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, os.path.relpath(image_path, directory))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                resize_image(image_path, output_path, width, height)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Resize images in a directory.')
    parser.add_argument('size', type=str, help='Target size in WIDTHxHEIGHT format (e.g., 1920x1080)')
    
    args = parser.parse_args()
    
    # Parse the width and height from the input string
    try:
        width, height = map(int, args.size.lower().split('x'))
    except ValueError:
        print("Invalid size format. Please use WIDTHxHEIGHT (e.g., 1920x1080).")
        exit(1)

    # Set your input and output directories relative to the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(script_directory, "input")  # Change this to your input directory
    output_directory = os.path.join(script_directory, "output")  # Change this to your output directory
    
    resize_images_in_directory(input_directory, output_directory, width, height)
