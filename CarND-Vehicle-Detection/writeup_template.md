##Writeup Template
###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Vehicle Detection Project**

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

[//]: # (Image References)
[image1]: ./output_images/sample_car_not_car.png
[image2]: ./output_images/hog_vis.png
[image3]: ./output_images/with_cars.png
[image4]: ./output_images/no_cars.png
[image5]: ./examples/bboxes_and_heat.png
[image6]: ./examples/labels_map.png
[image7]: ./examples/output_bboxes.png
[video1]: ./project_video.mp4

## [Rubric](https://review.udacity.com/#!/rubrics/513/view) Points
###Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  


###Histogram of Oriented Gradients (HOG)

####1. Explain how (and identify where in your code) you extracted HOG features from the training images.

The code for this step is contained in the 19th code block in the function `get_hog_features`. 

I started by reading in all the `vehicle` and `non-vehicle` images.  Here is an example of one of each of the `vehicle` and `non-vehicle` classes:

![alt text][image1]

Here is an example using the `YCrCb` color space and HOG parameters of `orientations=9`, `pixels_per_cell=(8, 8)` and `cells_per_block=(2, 2)`:


![alt text][image2]

####2. Explain how you settled on your final choice of HOG parameters.

I tried various color spaces and decided on using the YCrCb specifically due to its capability to 1) capture the overall gradient information in channel 1. 2) Capture information about color features specific to vehicles. This can be seen in the image shown above where channel 2 captures the indicator lights of the random vehicle displayed.

For processing time convenience, I resized the image to `32x32` instead of the original `64x64` size. This drastically reduced the number of windows over which the algorithm had to compute. Overall my HOG features made up only `972` values out of the final feature vector size of `4092`.

####3. Describe how (and identify where in your code) you trained a classifier using your selected HOG features (and color features if you used them).

Code block seven defines a linear support vector machine classifier and a grid search function which searches across 5 logarithmic decades `[0.001, 10]` for the optimal `C` parameter (The optimal value was 0.001 with roughly 0.98 test accuracy). The data used came from the GTI, KITTI and Udacity dataset. Apart from the HOG features, color histogram and spatial bin features were also used for the classification. The images sizes used for the latter two features were both `32X32`. 

###Sliding Window Search

####1. Describe how (and identify where in your code) you implemented a sliding window search.  How did you decide what scales to search and how much to overlap windows?

The search was restricted to roughly the right three quarters of the image i.e. `x > 400` and the roughly the lower third quartile along the vertical axis i.e. ` 400 < y < 700 `. Code block 9 contains the code that performs the sliding window search. The scales for detecting the vehicles `3 and 4` were picked such that both partial features and the overall view of the vehicles could be captured, in the range of search of the sliding window search.

####2. Show some examples of test images to demonstrate how your pipeline is working.

Ultimately I searched on two scales using YCrCb 3-channel HOG features plus spatially binned color and histograms of color in the feature vector, which provided a nice result.  Here are some example images:

![alt text][image3]
![alt text][image4]
---

### Video Implementation

####1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (somewhat wobbly or unstable bounding boxes are ok as long as you are identifying the vehicles most of the time with minimal false positives.)
Here's a [link to my video result](./base_output.mp4)


####2. Describe how (and identify where in your code) you implemented some kind of filter for false positives and some method for combining overlapping bounding boxes.

I implemented a class that would average the detected bounding boxes over `15 frames`. The positions are stored as a heat map and thresholded to obtain regions with high confidence of detection. 
The averaging in time smoothens the detections and rejects some of the false detection which are thresholded out. A `cv2.GaussianBlur` is applied in space, to smoothen the boundaries of the bounding boxes. Finally, `scipy.ndimage.measurements.label` is used to distinguish the individual instances of detections.

Here's a [link to my video result with the heat map blended](./base_output_with_heat.mp4)



---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

The computation of the HOG features at the original dimensions of the image took a long period of time (around 1 hour to evaluate a video of 50 seconds long). After the resizing, it now takes roughly 5 minutes. The pipeline would likely fail in regions where the camera data is drastically anomalous compared to the situations in the training samples e.g. when the image is really dark. Further input data from active sensing such as a lidar or a laser scanner could be used to robustify the final detection.

