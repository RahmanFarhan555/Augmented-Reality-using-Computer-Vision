# Augmented-Reality-using-Computer-Vision
 The goal is to develop an algorithm capable of detecting ArUco markers in the images and
 accurately placing AR images in their respective positions. By leveraging computer vision
 techniques, particularly with libraries like OpenCV, the aim to seamlessly integrate digital
 content, such as a poster, into real-world environments. This involves precise marker detection to determine the 3D positioning of the scene, enabling the proper alignment of AR
 elements. Through this project, I seek to showcase the potential of augmented reality
 technology in enhancing interior spaces, providing insights into the practical application
 of computer vision for AR applications

 1. Loading the Original Image:
 • image = cv2.imread(‘images/image 1.jpg’): This line loads an image named
 ’image 1.jpg’ from the ’images’ folder using the OpenCV function cv2.imread().
 The loaded image is stored in the variable image.

 2. Converting to Grayscale:
 • gray = cv2.cvtColor(image, cv2.COLOR BGR2GRAY): This line converts the
 loaded color image (image) to grayscale using the OpenCV function cv2.cvtColor().
 Grayscale images are easier to process and reduce computational complexity.

 3. Defining ArUco Dictionary and Parameters:
 • aruco dict =cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT 6X6 250): Here,
 an ArUcodictionary is initialized using the function cv2.aruco.getPredefinedDictionary().
 The dictionary type chosen is cv2.aruco.DICT 6X6 250, which specifies a dictionary of 6x6 ArUco markers with 250 unique IDs.
 • parameters = cv2.aruco.DetectorParameters(): Detector parameters are defined using the cv2.aruco.DetectorParameters() function. These parameters
 control the behavior of the ArUco marker detection algorithm, such as corner
 refinement and marker size thresholds.

 4. Detecting Markers:
 • corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco dict,
 parameters=parameters): ArUco markers are detected in the grayscale image
 (gray) using the cv2.aruco.detectMarkers() function. This function returns
 the corners of detected markers (corners), their corresponding IDs (ids), and
 rejected points (rejectedImgPoints).

 5. Loading the Replacement Image:
 • replacement image = cv2.imread(‘images/overlay image.jpg’): Another im
age, named ‘overlay image.jpg’, is loaded from the ’images’ folder using cv2.imread().
 This image will be overlaid onto the detected markers.

 6. Calculating Replacement Image Dimensions:
 • replacement height, replacement width = replacement image.shape[:2]: The
 height and width of the replacement image are obtained using the shape at
tribute of the NumPy array representing the image.

 7. Defining a Scale Factor:
 • scale factor = 6: A scale factor is defined to adjust the size of the replacement
 image relative to the size of the detected markers. This factor determines how
 much the replacement image will be enlarged.

 8. Iterating Through Detected Markers:
 • for i in range(len(ids)):: A loop iterates through each detected marker.
 The subsequent lines within the loop perform the following tasks:
 • Computing New Corner Points: The corner points of the detected marker
 are used to compute new corner points for enlarging the replacement image
 based on the scale factor.
 • Performing Perspective Transformation: A perspective transformation
 is applied to the replacement image to align it with the detected marker using
 cv2.getPerspectiveTransform() and cv2.warpPerspective().
 • Creating a Mask: A mask is created to define the region of interest for
 blending the replacement image with the original image.
 • Blending Images: The replacement image is combined with the original image using bitwise operations (cv2.bitwise and() and cv2.bitwise or()) to overlay
 it on the detected marker.

 ![image](https://github.com/RahmanFarhan555/Augmented-Reality-using-Computer-Vision/assets/170820777/818dc9b1-8691-4961-a96f-21bfce3bd72e)
 ![image](https://github.com/RahmanFarhan555/Augmented-Reality-using-Computer-Vision/assets/170820777/76aff7be-c6b9-40a7-a459-49f4cd3d0cf1)
 ![image](https://github.com/RahmanFarhan555/Augmented-Reality-using-Computer-Vision/assets/170820777/00ad3c9d-0fd8-4cce-be3d-996cff2d8fc8)




 Finally, the processed image with overlaid ArUco markers is displayed in a
 window using cv2.imshow(), and the program waits for a key press before
 closing the window using cv2.waitKey() and cv2.destroyAllWindows().
