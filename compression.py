import os
from PIL import Image

def compress_image(image_path, output_path, quality):
    try:
        with Image.open(image_path) as img:
            if img.format in ['JPEG', 'JPG']:
                # Copy JPEG files directly without compressing
                img.save(output_path, optimize=True, quality=100)
                print(f"Copied {image_path} without compression as {output_path}")
            else:
                img.convert('RGB').save(output_path, format='JPEG', optimize=True, quality=quality)
                print(f"Compressed {image_path} and saved as {output_path} with quality={quality}")
    except Exception as e:
        print(f"Error compressing {image_path}: {e}")

def compress_images_in_directory(directory, output_directory, quality):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
                image_path = os.path.join(root, file)
                output_path = os.path.join(output_directory, os.path.relpath(image_path, directory))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                compress_image(image_path, output_path, quality)

if __name__ == "__main__":
    # Set your input and output directories relative to the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(script_directory, "input")
    output_directory = os.path.join(script_directory, "output")
    
    # Set your desired quality level
    desired_quality = 99  # Adjust this value for desired compression quality
    
    compress_images_in_directory(input_directory, output_directory, quality=desired_quality)
