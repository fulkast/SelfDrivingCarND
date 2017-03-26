#**Traffic Sign Recognition** 

##Writeup Template

###You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.

---

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:
* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./training_data_dist.png 
[image2]: ./validation_data_dist.png 
[image3]: ./testing_data_dist.png 
[image4]: ./german_traffic_sign_data/no_enter.jpg "Traffic Sign 1"
[image5]: ./german_traffic_sign_data/50.jpg "Traffic Sign 2"
[image6]: ./german_traffic_sign_data/priority.jpg "Traffic Sign 3"
[image7]: ./german_traffic_sign_data/yield.jpg "Traffic Sign 4"
[image8]: ./german_traffic_sign_data/stop.jpg "Traffic Sign 5"
[image9]: ./sample_test_output.png "Output From Classifying the Five Images Found Online"

[image10]: ./featureMap.png

## Rubric Points
###Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
###Writeup / README

####1. Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf. You can use this template as a guide for writing the report. The submission includes the project code.

You're reading it! and here is a link to my [project code](https://github.com/fulkast/SelfDrivingCarND/blob/master/CarND-Traffic-Sign-Classifier-Project/Traffic_Sign_Classifier.ipynb)

###Data Set Summary & Exploration

####1. Provide a basic summary of the data set and identify where in your code the summary was done. In the code, the analysis should be done using python, numpy and/or pandas methods rather than hardcoding results manually.

The code for this step is contained in the second code cell of the IPython notebook.  

I used the standard python methods to generate a summary of the data sets used for training and testing.

* The size of training set is 34799
* The size of test set is 12630
* The shape of a traffic sign image is (32,32)
* The number of unique classes/labels in the data set is 43

####2. Include an exploratory visualization of the dataset and identify where the code is in your code file.

The code for this step is contained in the third code cell of the IPython notebook.  

Here is an exploratory visualization of the data set. Below are bar charts showing the distributions of the traffic sign classes used in the training, validation and testing phase.

![alt text][image1]
![alt text][image2]
![alt text][image3]


###Design and Test a Model Architecture

####1. Describe how, and identify where in your code, you preprocessed the image data. What tecniques were chosen and why did you choose these techniques? Consider including images showing the output of each preprocessing technique. Pre-processing refers to techniques such as converting to grayscale, normalization, etc.

The code for this step is contained in the fourth code cell of the IPython notebook.

I did not convert the images to grayscale. The different sign classes have different color information, some have primarily blue boundaries and others have primarily red boundaries. Hence, I decided to maintain the color information.

I did, however, normalize the image, this is so that the Euclidean norm of the data stay relatively low. I did this for the purpose of maintaining numerical stability, since performing arithmetic on large scalars, repetitively may lead to inaccuracies. Moreover, at a low magnitude, the different log propabilities of the logits of the different classes are also more distinguishable from each other. 

####2. Describe how, and identify where in your code, you set up training, validation and testing data. How much data was in each set? Explain what techniques were used to split the data into these sets. (OPTIONAL: As described in the "Stand Out Suggestions" part of the rubric, if you generated additional data for training, describe why you decided to generate additional data, how you generated the data, identify where in your code, and provide example images of the additional data)


To cross validate my model, used the validation data set which came with the originally downloaded data.

My final training set had 34799 number of images. My validation set and test set had 12630 and Z number of images.
 

####3. Describe, and identify where in your code, what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

The code for my final model is located in the fifth cell of the ipython notebook. 

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x3 RGB image   							| 
| Convolution 3x3     	| 1x1 stride, same padding, outputs 32x32x32 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 16x16x64 				|
| Convolution 3x3	    | 1x1 stride, same padding, outputs 10x10x32 	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x32 		    		|
| Flatten	         	| Output 800x1     	                            |
| Fully connected		| Output 120x1 									|
| RELU					|												|
| Fully connected		| Output 84x1 									|
| RELU					|												|
| Fully connected		| Output n_classesx1 			                |
| Softmax				| etc.        									|
|						|												|
|						|												|
 


####4. Describe how, and identify where in your code, you trained your model. The discussion can include the type of optimizer, the batch size, number of epochs and any hyperparameters such as learning rate.

The code for training the model is located in the seventh cell of the ipython notebook. 

To train the model, I used the ADAM optimizer to minimize the cross entropy between the output logits (of the different classes) from the model and the one hot vector of the correct class, as given during training. The batch size is 128, the training had 50 epochs and the learning rate was a mild 0.001.

####5. Describe the approach taken for finding a solution. Include in the discussion the results on the training, validation and test sets and where in the code these were calculated. Your approach may have been an iterative process, in which case, outline the steps you took to get to the final solution and why you chose those steps. Perhaps your solution involved an already well known implementation or architecture. In this case, discuss why you think the architecture is suitable for the current problem.

The code for calculating the accuracy of the model is located in the sixth cell of the Ipython notebook.

My final model results were:
* training set accuracy of 0.99
* validation set accuracy of 0.944
* test set accuracy of 0.926

If an iterative approach was chosen:
* What was the first architecture that was tried and why was it chosen?

The Lenet architecture from the digit recognition example was used at first. It is a strong architecture, well designed, and designated for a similar image recognition task.
* What were some problems with the initial architecture? 

The initial model gave low validation accuracy.
* How was the architecture adjusted and why was it adjusted? Typical adjustments could include choosing a different model architecture, adding or taking away layers (pooling, dropout, convolution, etc), using an activation function or changing the activation function. One common justification for adjusting an architecture would be due to over fitting or under fitting. A high accuracy on the training set but low accuracy on the validation set indicates over fitting; a low accuracy on both sets indicates under fitting.

To improve the LeNet architecture, I began by increasing the dimensionality of the first convolution layer to 32 independent slices. My reasoning was that, compared to recognizing digits, there are now more low level features that need to be extracted for the purpose of traffic sign recognition.

* What are some of the important design choices and why were they chosen? For example, why might a convolution layer work well with this problem? How might a dropout layer help with creating a successful model?

Additionally, I created a dropout layer after the second convolution+max_pooling layer, with a drop out rate of 50%. I did so to tackle the overfitting of the model, as the model was performing better on the training set than on the validation set.

###Test a Model on New Images

####1. Choose five German traffic signs found on the web and provide them in the report. For each image, discuss what quality or qualities might be difficult to classify.

Here are five German traffic signs that I found on the web:

![alt text][image4] ![alt text][image5] ![alt text][image6] 
![alt text][image7] ![alt text][image8]

The first image might be difficult to classify because of the skew of the orientation of the traffic sign, when compared to the standard sign in the training set. This orientation anomaly aspect also applies to the stop sign image, where the sign is slightly tilted. The remainder of the images are pretty standard, with the minor caveat that they are overlayed by a watermark mask, which cites the source of the image.

####2. Discuss the model's predictions on these new traffic signs and compare the results to predicting on the test set. Identify where in your code predictions were made. At a minimum, discuss what the predictions were, the accuracy on these new predictions, and compare the accuracy to the accuracy on the test set (OPTIONAL: Discuss the results in more detail as described in the "Stand Out Suggestions" part of the rubric).

The code for making predictions on my final model is located in the ninth cell of the Ipython notebook.

Here are the results of the prediction:

| Image			        |     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| No Entry Sign   		| No Entry Sign									| 
| Speed limit 50  		| Speed limit 50								|
| Priority zone			| Priority zone									|
| Yield sign	   		| Yield sign					 				|
| Stop sign	    		| Stop sign         							|


The model was able to correctly guess 5 of the 5 traffic signs, which gives an accuracy of 100%. This compares favorably to the accuracy on the test set of 92.6%.
The result from cell nine in my code shows, for each image, two sub plots. The single subplot on the left shows the image from the test set. The five plots on the right show the images from the training set with the top 5 softwmax probabilities.

Below is an example of the output

![alt text][image9]

####3. Describe how certain the model is when predicting on each of the five new images by looking at the softmax probabilities for each prediction and identify where in your code softmax probabilities were outputted. Provide the top 5 softmax probabilities for each image along with the sign type of each probability. (OPTIONAL: as described in the "Stand Out Suggestions" part of the rubric, visualizations can also be provided such as bar charts)

The code for making predictions on my final model is located in the 9th cell of the Ipython notebook.

For all the images taken from the web, the output softmax probabilities of the prediction was a stunning 100%. The model is pretty confident in its outputs.

| Probability         	|     Prediction	        					| 
|:---------------------:|:---------------------------------------------:| 
| 1.00         			|  No Entry Sign								| 
| 1.00          		| Speed limit 50								|
| 1.00	        		| Priority zone									|
| 1.00 	        		| Yield sign					 				|
| 1.00 	        		| Stop sign         							|


Additionally, I've used the outputFeatureMap method provided to explore the emphasis of different layers

The figure below shows the activation at the first layer to the yield sign. It demonstrates how some neurons are triggered by edges of a certain orientation, at the boundaries of the sign. E.g. featureMap 0 focuses on the positively sloped boundaries whereas featureMap 21 focuses on the negatively sloped boundaries.

![alt text][image10]
