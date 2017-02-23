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

[masked_image]: ./output_images/input_after_mask.png "White Color Mask"

[focused_image]: ./output_images/input_masked_focused.png "White Color Mask"


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



###2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


###3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...