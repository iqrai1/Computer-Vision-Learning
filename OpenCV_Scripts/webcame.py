import cv2

# Initialize the webcam
webcam = cv2.VideoCapture(0)

# Continuously capture frames
while True:
    ret, frame = webcam.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame in a window
    cv2.imshow('frame', frame)

    # Wait for 40ms, and break the loop if 'q' is pressed
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
webcam.release()
cv2.destroyAllWindows()
