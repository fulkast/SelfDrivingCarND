# Advanced Lane Finding Project

The following steps are carried out:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms and gradients to filter out the lanes
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./output_images/undistort.png "Undistorted"
[image2]: ./output_images/binary_combo_united.png "Binary Union of Filters"
[image3]: ./output_images/binary_combo.png "Binary Example"
[image4]: ./output_images/warped_straight_lines.png "Warp Example"
[image5]: ./examples/color_fit_lines.jpg "Fit Visual"
[image6]: ./examples/example_output.jpg "Output"
[video1]: ./project_video.mp4 "Video"

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Camera Calibration

The code for this step is contained in the "Camera Calibration" section in the IPython notebook located in "advanced_lane_finder.ipynb".

I begin globbing all the calibration images which are 2-D planar chessboard patterns of 9X6 in corners in dimension.
A visualization of these chessboard corner points are shown in code block 7. It is assumed that the 9X6 points used to calculate distortion parameters lie on a 2-D plane. In code block 9 the code, iterates through all the images in the calibration folder and there where 9X6 corner points have been successfully been detected, the corresponding points are appended. 
I then used `cv2.calibrateCamera()` function to calculate the distortion parameters.  I applied this distortion correction to the test image using the `cv2.undistort()` function and obtained this result: 

![alt text][image1]

### Pipeline (single images)

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image, using the helper functions in code block 14 in the ipython notebook.  Here's an example of my output for this step.  (note: this is not actually from one of the test images)

![alt text][image3]
![alt text][image2]

#### 3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

Code blocks 12 and 13 contain the code for the perspective transform. I used the `cv2.getPerspectiveTransform()` function to get the warping parameters. The source and destination points are hardcoded points designed to map from an image where the lanes are assumed to the straight (but converging due to the depth and perspective of the camera) to an image where the lanes are strictly straight. The points used are as follows:

| Source        | Destination   | 
|:-------------:|:-------------:| 
| 299, 652      | 199, 702      | 
| 594, 451      | 199, 150      |
| 1008, 652     | 908, 702      |
| 685, 451      | 908 , 150     |

I verified that my perspective transform was working as expected by drawing the `src` and `dst` points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image.

![alt text][image4]

#### 4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

Then I did some other stuff and fit my lane lines with a 2nd order polynomial kinda like this:

![alt text][image5]

#### 5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

I did this in lines # through # in my code in `my_other_file.py`

#### 6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

I implemented this step in lines # through # in my code in `yet_another_file.py` in the function `map_lane()`.  Here is an example of my result on a test image:

![alt text][image6]

---

### Pipeline (video)

#### 1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video.mp4)

---

### Discussion

#### 1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

Here I'll talk about the approach I took, what techniques I used, what worked and why, where the pipeline might fail and how I might improve it if I were going to pursue this project further.  
