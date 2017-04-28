# Behavioral Cloning Project

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image2]: ./examples/centerdriving.png
[image4]: ./examples/placeholder_small.png "Left Image"
[image5]: ./examples/placeholder_small.png "Right Image"
[image6]: ./examples/preflip.png "Normal Image"
[image7]: ./examples/postflip.png "Flipped Image"

---
## Files Submitted & Code Quality

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

## Model Architecture and Training Strategy 

My model follows the nVidia self-driving architecture. I begin by normalizing the data. Thereafter, three 2D-convolutional layers follow. Each of these has a relu activation non-linearity and a 5x5 filter. The depth after the final layer here is 48. Following this procedure, a 3X3 filtere, 2D-convolutional layer with a relu activation is introduced. The depth after this layer is 64. To prevent over-fitting, the output of this layer is passed through a dropout with 0.5 retention rate. It is then followed by an identical convolutional layer. Thereafter, the data is flattened and passed through three fully-connected layers, the first of which, has an l2-norm regularizer to prevent overfitting. (model.py lines 51-70)

#### Attempts to reduce overfitting in the model

The model contains a dropout layer and an l2-norm regularizer in order to reduce overfitting (model.py lines 62 and 65). 

The model was trained and validated on different data sets to ensure that the model was not overfitting (code line 10-16). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

#### Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 72).

#### Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road. Special attention was made, to ensure that the data contained enough scenes from the anomalous regions of the track e.g. the bridge and the regions where the curb was muddy.

For details about how I created the training data, see the next section. 

## Model Architecture and Training Strategy

#### Solution Design Approach

The overall strategy for deriving a model architecture was to start from the simplest model and then introduce complexity until the car can "almost always" drive correctly. Then, I would either improve the regularization or introduce more data to fit the scenarios where the car doesn't drive correctly. 

My first step was to use a convolution neural network model that was a simple regressor with one layer.

The validation and training error using this simple model, trained over 100 epochs was somewhat oscillatory. The errors kept rising and falling through a very wide range. This shows that the model is somewhat too simple to converge to a consistent optimal state. Nonetheless, this minimally designed model could actually drive the car around track one. However, the driving behavior was very erratic. The car kept swinging from the left of the track to the right, and vice versa, only correcting its behavior at the verge of rolling off the lanes.

For my next step, I moved on to a more powerful model - the one used by nVidia. The original implementation shared in the video lectures did not have regularization. Therefore, I added the two regularization techniques mentioned above. The training results were good, with the validation error being slightly larger than the training error - by 20%

The final step was to run the simulator to see how well the car was driving around track one. The results of this model were also slightly oscillatory in terms of the car swinging back and forth from left to right on the track. From this I conclude that own driving which was used to training the model was probably too erratic. 

The vehicle however, was able to stay on the track at all times. The passengers would be safe, but may experience sensations of nausea.


#### Creation of the Training Set & Training Process

Here is an example image of center lane driving:

![alt text][image2] 

To augment the data sat, I also flipped images and angles thinking that this would help mitigate the bias in the driving data caused by the counter-clockwise nature of track 1. For example, here is an image that has then been flipped:

![alt text][image6]
![alt text][image7]

I also used the left and right camera images as was done in the nVidia project. The corresponding steering angles to these images were adjusted by 0.5.

After the collection process, I had 14820 number of data points. I then used half of these for training and the other half for validation.


I finally randomly shuffled the data set and put 50% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. The ideal number of epochs was 10 as evidenced by the monotonic drop in the validation error. I used an adam optimizer so that manually training the learning rate wasn't necessary.
