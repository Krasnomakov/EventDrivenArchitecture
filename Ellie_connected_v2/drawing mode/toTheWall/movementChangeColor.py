import cv2
import numpy as np
from contourwall import ContourWall
import random
import time

# Define the dimensions for the pixelated image
pixelated_width, pixelated_height = 20, 20

# Define the dimensions for the enlarged pixelated display
display_width, display_height = 400, 400

# Open the camera
cap = cv2.VideoCapture(0)

# Initialize ContourWall
cw = ContourWall()
cw.single_new_with_port("COM4")

# Initialize a canvas for drawing
canvas = None

# Initialize the long exposure frame
long_exposure_frame = None

# Initialize variables for motion detection
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

motion_detected = False

# Initialize the persistent pixel data for ContourWall
persistent_pixels = np.zeros((pixelated_height, pixelated_width, 3), dtype=np.uint8)

# Function to enhance contrast
def enhance_contrast(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final

# Function to quantize colors to the nearest primary RGB values with intensity
def quantize_colors(image):
    quantized = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            pixel = image[i, j]
            r, g, b = pixel[0], pixel[1], pixel[2]
            r = 255 if r > 127 else 0
            g = 255 if g > 127 else 0
            b = 255 if b > 127 else 0
            quantized[i, j] = [r, g, b]
    return quantized

# Initialize pixel positions for floating effect
original_positions = [(j, i) for i in range(pixelated_height) for j in range(pixelated_width)]
pixel_positions = original_positions.copy()

# Function to apply floating effect
def apply_floating_effect(positions):
    global motion_detected
    if motion_detected:
        for index in range(len(positions)):
            x, y = positions[index]
            # Increase velocity significantly if motion is detected
            x += random.choice([-2, -1, 0, 1, 2])
            y += random.choice([-2, -1, 0, 1, 2])

            # Ensure positions are within bounds
            x = max(0, min(pixelated_width - 1, x))
            y = max(0, min(pixelated_height - 1, y))

            positions[index] = (x, y)
    else:
        positions[:] = original_positions[:]

# Function to send the pixelated data to ContourWall with persistence
def send_to_contour_wall(cw, current_pixels, persistent_pixels):
    for i in range(pixelated_height):
        for j in range(pixelated_width):
            # Only update the pixel if there is a significant change
            if not np.array_equal(current_pixels[i, j], persistent_pixels[i, j]):
                # Convert BGR to RGB for ContourWall
                color = current_pixels[i, j][::-1]
                cw.pixels[i, j] = color
                # Update persistent pixels
                persistent_pixels[i, j] = current_pixels[i, j]
    cw.show()

# Function to draw motion areas
def draw_motion_areas(frame_diff, pixelated):
    contours, _ = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 50:  # Filter out small contours
            x, y, w, h = cv2.boundingRect(contour)
            # Draw a colored rectangle over the detected motion area
            cv2.rectangle(pixelated, (x, y), (x + w, y + h), (0, 255, 255), -1)  # Yellow brush

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if frame is captured
    if not ret:
        break

    # Enhance the contrast of the frame
    frame = enhance_contrast(frame)

    # Convert frame to grayscale for motion detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Compute the absolute difference between the current frame and the previous frame
    frame_diff = cv2.absdiff(prev_gray, gray_frame)
    threshold_frame = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)
    
    # Check if there is any motion detected
    motion_detected = np.sum(threshold_frame) > 10000

    # Update previous frame
    prev_gray = gray_frame

    # Resize the frame to the desired dimensions (20x20) to pixelate it
    pixelated = cv2.resize(frame, (pixelated_width, pixelated_height), interpolation=cv2.INTER_LINEAR)

    # Quantize the colors to primary RGB values
    pixelated = quantize_colors(pixelated)

    # Draw motion areas on the pixelated image
    draw_motion_areas(threshold_frame, pixelated)

    # Initialize the canvas if it's None
    if canvas is None:
        canvas = np.zeros((display_height, display_width, 3), dtype=np.uint8)

    # Create a blank frame for drawing circles
    circle_frame = np.zeros((display_height, display_width, 3), dtype=np.uint8)

    # Apply the floating effect
    apply_floating_effect(pixel_positions)

    # Calculate the radius and spacing for the circles
    radius = display_width // pixelated_width // 2
    spacing_x = display_width // pixelated_width
    spacing_y = display_height // pixelated_height

    # Draw circles for each pixel
    for idx, (x, y) in enumerate(pixel_positions):
        color = pixelated[y, x]
        center_x = x * spacing_x + spacing_x // 2
        center_y = y * spacing_y + spacing_y // 2
        cv2.circle(circle_frame, (center_x, center_y), radius, color.tolist(), -1)

    # Add the current frame to the long exposure frame
    if long_exposure_frame is None:
        long_exposure_frame = np.zeros_like(circle_frame, dtype=np.float32)
    long_exposure_frame = cv2.addWeighted(long_exposure_frame, 0.95, circle_frame.astype(np.float32), 0.05, 0)

    # Apply the waterfall effect by shifting the pixels downward
    long_exposure_frame = np.roll(long_exposure_frame, 1, axis=0)

    # Convert the long exposure frame to 8-bit
    long_exposure_frame_8bit = cv2.convertScaleAbs(long_exposure_frame)

    # Combine the canvas with the long exposure frame
    combined_frame = cv2.addWeighted(long_exposure_frame_8bit, 0.7, canvas, 0.3, 0)

    # Display the combined frame
    cv2.imshow('Pixelated', combined_frame)

    # Send the pixelated data to ContourWall with persistence
    send_to_contour_wall(cw, pixelated, persistent_pixels)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

# Clear ContourWall pixels
cw.fill_solid(0, 0, 0)
cw.show()
