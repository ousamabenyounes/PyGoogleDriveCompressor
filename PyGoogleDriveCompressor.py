import os
import shutil
from PIL import Image

# Folder for moved original images
TARGET_DIRECTORY = "/content/drive/MyDrive/try"
ORIGINALS_FOLDER = os.path.join(TARGET_DIRECTORY, "originals_pictures")  # Folder for original images

# Minimum file size to process (in MB)
MIN_SIZE_MB = 0.5  # Ignore files smaller than this size

# Image compression function
def compress_image(input_path, output_path, quality=80):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=img.format, optimize=True, quality=quality)

        original_size = os.path.getsize(input_path) / (1024 * 1024)  # Convert to MB
        compressed_size = os.path.getsize(output_path) / (1024 * 1024)
        saved_mb = original_size - compressed_size
        compression_percentage = (saved_mb / original_size) * 100 if original_size > 0 else 0

        return True, saved_mb, compression_percentage

    except Exception as e:
        print(f"❌ Error compressing {input_path}: {e}")
        return False, 0.0, 0.0

# Function to process a specific directory
def process_directory(directory):
    if not os.path.exists(directory):
        print(f"❌ Directory does not exist: {directory}")
        return

    images = [f for f in os.listdir(directory) if f.lower().strip().endswith((".jpg", ".jpeg", ".png"))]

    if not images:
        print(f"❌ No image files found in the directory: {directory}")
        return

    print(f"📂 Processing directory: {directory} ({len(images)} images found)")

    os.makedirs(ORIGINALS_FOLDER, exist_ok=True)

    total_saved_space = 0.0  # Total space saved

    for image in images:
        img_path = os.path.join(directory, image)

        # Skip already compressed images
        if "_compressed" in image:
            print(f"⚠️ Skipping {image}: Already compressed.")
            continue  

        compressed_path = os.path.join(directory, image.replace(".", "_compressed."))

        # Check file size
        original_size = os.path.getsize(img_path) / (1024 * 1024)
        if original_size < MIN_SIZE_MB:
            print(f"❌ Skipping {image}: File too small ({original_size:.2f} MB).")
            continue  

        # Compress the image
        success, saved_mb, compression_percentage = compress_image(img_path, compressed_path)

        if success:
            total_saved_space += saved_mb
            print(f"✅ Compressed: {compressed_path} | {saved_mb:.2f} MB saved | {compression_percentage:.2f}% reduction")

            # Move the original image immediately after a successful compression
            try:
                shutil.move(img_path, os.path.join(ORIGINALS_FOLDER, image))
            except Exception as e:
                print(f"❌ Error moving {image}: {e}")

        else:
            # Remove the failed compressed file if compression was not successful
            if os.path.exists(compressed_path):
                os.remove(compressed_path)
                print(f"🗑 Deleted corrupted compressed file: {compressed_path}")

    print(f"🚀 Total space saved: {total_saved_space:.2f} MB")

# Run the compression for the target directory
process_directory(TARGET_DIRECTORY)
