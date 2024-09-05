# Image Compression and Resizing With Python and Pillow

## resizer.py
A script for resizing images in a specified directory and saving them to an output directory. The script takes target dimensions as input and processes all images within a given folder, preserving the directory structure.

### Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

You can install the required library using pip:

```bash
pip install Pillow
```

### Resizing Images

To resize images, follow these steps:

Place Images in the input/ Folder: Put all the images you want to resize in the input directory.

Run the Resizing Script:

You can use one of the provided batch files to run the script.

Using the batch files:

run-resizer.bat: This batch file runs the script with default settings (1920 x 1080).

Example Usage from Command Line:

```
bash
python resizer.py 1920x1080
```

This command resizes all images in the input folder to 1920x1080 pixels and saves them in the output folder. Specify whichever resolution you want to use in the script.

### Notes:
-Ensure that the input and output directories are correctly set in the resize_images.py script if you need to adjust their paths.
-The script currently processes .jpg, .jpeg, .png, and .gif file formats.

### Troubleshooting:
-If you encounter issues, make sure the Pillow library is installed and correctly configured.
-Verify that the image dimensions provided are valid integers and formatted correctly (e.g., 1920x1080).


## compression.py

A script for compressing images in a specified directory and saving them to an output directory. The script compresses all images within a given folder, preserving the directory structure and converting non-JPEG images to JPEG format with a specified quality level.

### Requirements

- Python 3.x
- Pillow library (Python Imaging Library)

You can install the required library using pip:

```bash
pip install Pillow
```

### Compressing Images

To compress images, follow these steps:

1. **Place Images in the `input/` Folder**: Put all the images you want to compress in the `input` directory.

2. **Run the Compression Script**:

You can use one of the provided batch files to run the script.

Using the batch files:

run-compression.bat: This batch file runs the script with default settings.

```bash
python compression.py
```

This command compresses all images in the `input` folder using a default quality level of 99 and saves them in the `output` folder. You can adjust the `desired_quality` variable in the script to set a different quality level.

#### Notes
- Ensure that the input and output directories are correctly set in the `compress_images.py` script if you need to adjust their paths.
- The script currently processes `.jpg`, `.jpeg`, `.png`, and `.gif` file formats.
- JPEG files are copied without additional compression, while other formats are converted to JPEG and compressed.

#### Troubleshooting
- If you encounter issues, make sure the Pillow library is installed and correctly configured.
- Verify that the desired quality level is an integer between 0 and 100.