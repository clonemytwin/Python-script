import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the range of green color in the HSV color space
    lower_green = np.array([45, 100, 50])
    upper_green = np.array([75, 255, 255])


    # Create a binary mask where green pixels are True and non-green pixels are False
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Create a black image with the same size as the frame
    black = np.zeros_like(frame)

    # Use the binary mask to replace the green pixels in the frame with black pixels
    result = cv2.bitwise_and(frame, black, mask=mask)

    # Display the result
    cv2.imshow("Green Screen", result)

    # Break the loop if the "q" key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()

# Save the result as an image
cv2.imwrite("green_screen_result.jpg", result)

# Close all windows
cv2.destroyAllWindows()
