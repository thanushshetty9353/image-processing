import numpy as np
import cv2

def add_salt_and_pepper(image, salt_prob=0.01, pepper_prob=0.01):
    """Add salt and pepper noise to an image."""
    noisy = np.copy(image)
    total_pixels = image.size

    # Salt noise (white pixels)
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[salt_coords[0], salt_coords[1]] = 255

    # Pepper noise (black pixels)
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy[pepper_coords[0], pepper_coords[1]] = 0

    return noisy

def add_uniform_noise(image, low=0, high=50):
    """Add uniform noise to the image."""
    row, col, _ = image.shape
    uniform_noise = np.random.randint(low, high, (row, col, 3), dtype=np.uint8)


    noisy = cv2.add(image, uniform_noise)
    return noisy

def add_gaussian_noise(image, mean=0, sigma=25):
    """Add Gaussian noise to the image."""
    row, col, channels = image.shape
    gaussian_noise = np.random.normal(mean, sigma, (row, col, channels)).astype(np.uint8)
    noisy = cv2.add(image, gaussian_noise)
    return noisy


def remove_salt_and_pepper_noise(image):
    """Remove salt and pepper noise using a median filter."""
    return cv2.medianBlur(image, 5)  # 5x5 kernel size for median filtering

def remove_uniform_noise(image):
    """Remove uniform noise using Gaussian blur."""
    return cv2.GaussianBlur(image, (5, 5), 0)

def remove_gaussian_noise(image):
    """Remove Gaussian noise using Gaussian blur."""
    return cv2.GaussianBlur(image, (5, 5), 0)

def add_and_remove_noise(image_path):
    """Add noise to the image and remove it."""
    # Read the image
    image = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
    if image is None:
        raise FileNotFoundError(f"Cannot read the image file at {image_path}. Check the path and file integrity.")
    cv2.imshow('images',image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

# closing all open windows
    cv2.destroyAllWindows()
    # Add Salt and Pepper noise
    sp_noise = add_salt_and_pepper(image)
    
    cv2.imshow('images',sp_noise)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
    cv2.waitKey(0)

# closing all open windows
    cv2.destroyAllWindows()
    cv2.imwrite('../output/salt_and_pepper_noisy_image.jpeg', sp_noise)
    print("Salt and Pepper noise added and saved successfully!")

    # Remove Salt and Pepper noise
    cleaned_sp_image = remove_salt_and_pepper_noise(sp_noise)
    cv2.imwrite('../output/cleaned_sp_image.jpeg', cleaned_sp_image)
    print("Salt and Pepper noise removed and cleaned image saved successfully!")

    # Add Uniform noise
    uniform_noise = add_uniform_noise(image)
    cv2.imwrite('../output/uniform_noisy_image.jpeg', uniform_noise)
    print("Uniform noise added and saved successfully!")

    # Remove Uniform noise
    cleaned_uniform_image = remove_uniform_noise(uniform_noise)
    cv2.imwrite('../output/cleaned_uniform_image.jpeg', cleaned_uniform_image)
    print("Uniform noise removed and cleaned image saved successfully!")

    # Add Gaussian noise
    gaussian_noise = add_gaussian_noise(image)
    cv2.imwrite('../output/gaussian_noisy_image.jpeg', gaussian_noise)
    print("Gaussian noise added and saved successfully!")

    # Remove Gaussian noise
    cleaned_gaussian_image = remove_gaussian_noise(gaussian_noise)
    cv2.imwrite('../output/cleaned_gaussian_image.jpeg', cleaned_gaussian_image)
    print("Gaussian noise removed and cleaned image saved successfully!")

# Call the function with the image path

add_and_remove_noise('../input/input_image.jpeg')
