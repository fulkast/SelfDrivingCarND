#**Finding Lane Lines on the Road** 

##Writeup Template

###You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[raw_input_image]: ./output_images/111.jpg "Raw Input Image"

[yellow_mask]: ./output_images/yellow_mask.png "Yellow Color Mask"

[white_mask]: ./output_images/gray_mask.png "White Color Mask"

[final_mask]: ./output_images/gray_yellow_mask.png "Final Mask (Sum of Yellow and White)"

[masked_image]: ./output_images/input_after_mask.png "Masked Image"

[focused_image]: ./output_images/input_masked_focused.png "Masked and Focused Image"

[raw_lines]: ./output_images/raw_lines.png "Raw Lines"

[hull]: ./output_images/hull_contour.png "Hull Contour"

[slope_plot]: ./output_images/clustering_slopes.png "Slope Clusters"

[dividing_lane]: ./output_images/differentiated_lanes.png "Divided Lanes"

[final_lanes]: ./output_images/lanes_after_RANSAC.png "Final Lanes"

---

### Reflection

###1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline begins with the input image in RGB format. An example is shown below which was extracted from the challenge video. 

![alt text][raw_input_image]

Assuming that the lanes are either white or yellow, I proceed with transforming the image to the HSV space where the yellow color may be easily singled out. To isolate the white color information, I converted the original image into grayscale where the intensity can be used to find white colors. The following two images show the yellow and white masks respectively,

![alt text][yellow_mask]

![alt text][white_mask]

Using the bitwise-or operation the two masks are summed together to produce a mask that retains the yellow and white information as seen below.

The final mask:
![alt text][final_mask]

The masked input image:
![alt text][masked_image]

Next up, I select a polygonal region of interest that is roughly symmetric about the center of the image and extends from the bottom of the image to right about half way. 

The focused image:
![alt text][focused_image]

At this point it would be beneficial to be able to treate the points on the two lanes separately. To do this, I first extracted the lines using the Hough transform algorithm with a spatial resolution of 5 pixels, angular resolution of 5 degrees, vote threshold of 50 votes minimum, minimum line length of 10 and maximum line gap of 2. This results in the lines shown below.

![alt text][raw_lines]

From the vertices of these lines, we can extract the convex hull which encloses all the points. From the hull shape we can then extract center of mass using openCV's moments function. The resultant center of the lanes is shown below.

![alt text][hull]

To distinguish between the two lanes, another channel of information is used, namely the slope of the individual lines. Collecting the slopes together and running a K-means clustering into two clusters - with initial cluster centers at diametrically separated values away from zero - we can obtain the "aggregate" slopes of the two lanes. The figure below shows the distribution of the slopes for this working example and the corresponding slope cluster centers.

![alt text][slope_plot]

Using this information, as well as the horizontal moment of area of each line with respect to the center line, each line may be assigned to either the left or right lane. A line belongs to the left lane if its moment is negative and its slope clusters together with the left lane lines. The left lane cluster has the lower value of the two slope clusters.

The resultant separation is shown below:

![alt text][dividing_lane]

Next, the two lanes are post-processed separately. For each side, each point belonging to a line is fed into a RANSAC regressor, to learn the line while taking into consideration of outliers. Finally, the lane produced by predicting the value of the lane at the bottom of the screen as well as at a fixed height close to the middle of the screen. This is done for both lanes separately. 

![alt text][final_lanes]



###2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the lanes colors are drastically different from the assumed yellow and white colors. In that case, it would be beneficial to consider the union of different color masks, much like the approach taken here but extended to more colors.

Another drawback is the sensitivity to the tuning parameters. The approach used here relies on thresholding based on different colors. These thresholds depend on external factors such as light source changes, time of day etc. For the cases tested here however, the combination of the white and yellow mask seem to work well.


###3. Suggest possible improvements to your pipeline

A great way to improve the lane detector would be to take into account the continuous nature of the actual lanes and to store the pose of the lanes from the previous frame. This way we may have a sort of prior guess as to where the lanes would be, and build up from there. This would lead into smoother lane tracking.

It would also be beneficial to fit non-linear functions to the lanes. This way the tracker would be more robust at sharp turns, which are quite crucial.
