import cv2
from matplotlib import pyplot as plt

def apply_filters(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
    if image is None:
        raise FileNotFoundError(f"Cannot read the image file at {image_path}. Check the path and file integrity.")

    # Step 1: Convert to black and white
    bw_image = cv2.imread(image_path,  cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('../output/black_and_white.jpg', bw_image)

    # Step 2: Find and save the histogram
    plt.hist(image.ravel(), bins=256, range=[0, 256])
    plt.title("Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.savefig('../output/histogram.png')
    plt.close()

    # Step 3: Apply Mean Filter
    mean_filtered = cv2.blur(image, (5, 5))
    cv2.imwrite('../output/mean_filter.jpg', mean_filtered)

    # Step 4: Apply Average Filter
    average_filtered = cv2.boxFilter(image, -1, (5, 5))
    cv2.imwrite('../output/average_filter.jpg', average_filtered)

    print("Filters, histogram, and black-and-white conversion applied and saved successfully!")

# Call the function
apply_filters('..\input\input_image.jpeg')
