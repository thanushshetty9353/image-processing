# Image Processing Toolkit

## Overview
This project demonstrates various image processing techniques using Python's OpenCV library. It covers image filtering, noise addition/removal, and live webcam video feed processing.

### Key Features:
1. **Image Filtering and Histogram Analysis**  
   - Convert images to black and white.
   - Compute and save image histograms.
   - Apply Mean and Average filters to enhance image quality.

2. **Noise Addition and Removal**  
   - Add Salt and Pepper, Uniform, and Gaussian noise.
   - Remove noise using Median and Gaussian filters.

3. **Webcam Video Details**  
   - Capture live video feed from the webcam.
   - Display resolution, frame rate, and current frame number dynamically.

---

## Prerequisites
- **Python Version**: 3.x  
- **Libraries Required**:
  - OpenCV
  - NumPy
  - Matplotlib

Install dependencies using:
```bash
pip install opencv-python numpy matplotlib



Project Structure

├── input/
│   └── input_image.jpeg        # Input image for processing
├── output/
│   ├── black_and_white.jpg     # Grayscale version of the image
│   ├── histogram.png           # Image histogram
│   ├── mean_filter.jpg         # Mean filtered image
│   ├── average_filter.jpg      # Average filtered image
│   ├── salt_and_pepper_noisy_image.jpeg # Image with Salt and Pepper noise
│   ├── cleaned_sp_image.jpeg   # Image after cleaning Salt and Pepper noise
│   ├── uniform_noisy_image.jpeg # Image with Uniform noise
│   ├── cleaned_uniform_image.jpeg # Image after cleaning Uniform noise
│   ├── gaussian_noisy_image.jpeg # Image with Gaussian noise
│   └── cleaned_gaussian_image.jpeg # Image after cleaning Gaussian noise
└── main.py                    # Main script for applying filters and noise operations



