import cv2
import time

def get_webcam_video_details():
    # Open the webcam (0 is typically the default webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Couldn't open webcam.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Frame width
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Frame height
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames per second

    # Display the video details (initial values)
    print("Webcam Video Details:")
    print(f"Resolution: {frame_width}x{frame_height}")
    print(f"Frame Rate (FPS): {fps}")

    # Start time to calculate elapsed time
    start_time = time.time()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Show the current frame in a window
        cv2.imshow('Webcam Video', frame)

        # Calculate elapsed time based on the start time
        elapsed_time = time.time() - start_time

        # Calculate the current frame number
        current_frame_count = int(elapsed_time * fps)

        # Display live details of video while it is running
        print(f"Current Time: {elapsed_time:.2f} seconds, Frame: {current_frame_count}")

        # Press 'q' to quit the video capture window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture object and close the video window
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start webcam capture and display details
get_webcam_video_details()
