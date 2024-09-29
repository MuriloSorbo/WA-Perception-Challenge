# WA-Perception-Challenge

This project detects red color in an image, finds the contours of the red regions, and fits two lines based on the center points of the detected contours.

## Output Image

The generated image after running the code will be saved as `out.png`. An example image (`out.png`) is shown below:

![red.png](./red.png) | ![out.png](./out.png) 

## Methodology

### Steps:

1. **Read the Image**: 
   The image is read using OpenCV's `cv2.imread()` function from the file path `./red.png`.

2. **Convert to HSV**: 
   The image is converted to the HSV color space, which is better suited for color detection than BGR or RGB.

3. **Define HSV Range for Red**: 
   The red color range is defined using lower and upper bounds in the HSV space. These bounds are used to create a binary mask where red regions are white (255) and everything else is black (0).

4. **Dilate the Mask**: 
   To improve the detection, the mask is dilated using `cv2.dilate()` with a 10x10 kernel. Dilation helps to fill in small gaps in detected regions.

5. **Find Contours**: 
   The contours of the red regions are detected using `cv2.findContours()`. These contours represent the boundaries of the red objects in the image.

6. **Classify Points as Left or Right**: 
   The bounding boxes of each contour are used to calculate the center point (`cX`, `cY`). Points with `cX` values to the left of the image center are classified as `leftBorder` points, while those to the right are classified as `rightBorder`.

7. **Fit Lines Using Polyfit**: 
   `np.polyfit()` is used to fit a line to both the `leftBorder` and `rightBorder` points. This generates linear equations for each line.

8. **Draw the Lines**: 
   Using the linear equations, two lines are drawn on the image based on predicted points at `y = 10` and `y = height - 10`.

9. **Save the Result**: 
   The final image with the lines is saved as `out.png`.

## What Did You Try and Why Did It Not Work?

In the initial attempts:

- **Mask Accuracy**: The boundaries of the red regions were not always detected accurately, leading to poor line fitting. This was likely due to noise or gaps in the binary mask. This issue was mitigated by dilating the mask, which improved contour detection.
  
- **Point Classification**: Initially, points near the center of the image were sometimes misclassified as left or right points. The solution was to use the bounding box center (`cX`) to accurately divide the points based on the image width.

- **Line Fitting**: At times, the line fitting was unstable when too few points were present. This was improved by ensuring a sufficient number of contours were detected by tuning the dilation parameters and adjusting the HSV range.

## Libraries Used

1. **OpenCV (cv2)**:
   - Used for image processing tasks such as reading images, converting color spaces, dilating the mask, finding contours, drawing lines, and saving the final output image.

2. **NumPy**:
   - Used for numerical operations, including the creation of the mask, managing arrays for the contour points, and performing polynomial fitting to generate the linear equations for the lines.
