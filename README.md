
# PyGoogleDriveCompressor

**PyGoogleDriveCompressor** is a Python script that allows you to compress image files located in a Google Drive directory. It is designed to work seamlessly with Google Colab, and can be customized for various compression settings. The script ensures efficient image compression while keeping the quality intact. This project was 100% AI-generated.

## Installation

### Requirements
- Google Drive with the folder containing your images
- Google Colab or local Python environment
- `Pillow` library for image processing

### Steps to Use (via Google Colab)
1. **Mount Google Drive:**
   - Open Google Colab and run the following code to mount your Google Drive:
     ```python
     from google.colab import drive
     drive.mount('/content/drive')
     ```

2. **Upload the script to Google Colab:**
   - Copy the `PyGoogleDriveCompressor.py` script to your Google Drive and upload it to your Colab workspace.

3. **Run the Script:**
   - In Colab, run the following:
     ```python
     !python /content/drive/MyDrive/your_path/PyGoogleDriveCompressor.py
     ```
   - This will process the images in the specified directory.

4. **Check the Output:**
   - The script will show the compression results in the output and move original images to a separate folder (`originals_pictures`).

### Manual Installation (if not using Colab)
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/PyGoogleDriveCompressor.git
   ```

2. Install required dependencies:
   ```bash
   pip install Pillow
   ```

3. Run the script on your local machine:
   ```bash
   python PyGoogleDriveCompressor.py
   ```

## How It Works
The script works by:
- Searching for image files in a specified Google Drive directory.
- Checking if the file is already compressed (if the filename contains `_compressed`).
- Compressing the images if they are not already compressed and meet the size requirements.
- Moving the original files to a separate folder (`originals_pictures`).

### Example of Console Output
```plaintext
📂 Processing directory: /content/drive/MyDrive/try (17 images found)
✅ Compressed: /content/drive/MyDrive/try/Copie de IMG_20220517_190841_compressed.jpg | 4.09 MB saved | 78.76% reduction
✅ Compressed: /content/drive/MyDrive/try/Copie de IMG_20220516_204916_compressed.jpg | 4.20 MB saved | 80.22% reduction
⚠️ Skipping IMG_20220516_170818.jpg: File too small (0.25 MB).
✅ Compressed: /content/drive/MyDrive/try/Copie de IMG_20220517_152913_compressed.jpg | 3.95 MB saved | 77.92% reduction
✅ Compressed: /content/drive/MyDrive/try/Copie de IMG_20220515_155747_compressed.jpg | 3.97 MB saved | 83.36% reduction
⚠️ Skipping IMG_20220516_170820_compressed.jpg: Already compressed.
🚀 Total space saved: 44.34 MB
```


### Contributors

- **ChatGPT**: Code development
- **Ousama Ben Younes**: Prompt engineering

### How to Contribute

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally.
3. **Create a branch** for your feature or bug fix.
4. **Commit your changes**.
5. **Push your changes** to your fork.
6. **Open a Pull Request** to this repository.

## License
This project is open-source and licensed under the MIT License.
B