import cv2
import numpy as np

# Load the original image
image = cv2.imread('images/image_1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the dictionary of ArUco markers
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Define the parameters for marker detection
parameters = cv2.aruco.DetectorParameters_create()

# Detect markers in the image
corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

# Load the replacement image
replacement_image = cv2.imread('images/overlay_image.jpg')

# Get the height and width of the replacement image
replacement_height, replacement_width = replacement_image.shape[:2]

# Define a scale factor to increase the size of the replacement image
scale_factor = 5 # Adjust as needed

# Iterate through detected markers
if ids is not None:
    for i in range(len(ids)):
        # Extract corner points of the marker
        marker_corners = corners[i][0]

        # Compute the center of the marker
        center = np.mean(marker_corners, axis=0)

        # Compute the new corner points for the enlarged replacement image
        new_marker_corners = center + scale_factor * (marker_corners - center)

        # Recompute perspective transformation matrix based on the new corner points
        src_points = np.array([[0, 0], [replacement_width, 0], [replacement_width, replacement_height], [0, replacement_height]], dtype=np.float32)
        dst_points = np.array(new_marker_corners, dtype=np.float32)
        matrix = cv2.getPerspectiveTransform(src_points, dst_points)

        # Apply perspective transformation to the replacement image
        transformed_replacement = cv2.warpPerspective(replacement_image, matrix, (image.shape[1], image.shape[0]))

        # Define a mask for the replacement image
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, [dst_points.astype(int)], (255, 255, 255))
        mask_inv = cv2.bitwise_not(mask)

        # Black out the area of the marker in the original image
        image_bg = cv2.bitwise_and(image, mask_inv)

        # Combine the replacement image with the original image using the mask
        image_fg = cv2.bitwise_and(transformed_replacement, mask)
        image = cv2.add(image_bg, image_fg)

# Display the result
cv2.namedWindow('Detected ArUco Markers', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Detected ArUco Markers', image.shape[1], image.shape[0])  # Resize the window to match image size
cv2.imshow('Detected ArUco Markers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
