# Neural Network Image Classifier

This project implements a deep neural network for the purpose of classifying objects relevant to self-driving cars: stop signs, cars, motorcycles, traffic lights, city buses, and fire hydrants. 

This project was completed in spring 2018 with the instruction and materials kindly provided to me by Max Lundgren, a graduate student studying machine learning and music at the University of Minnesota. I have only recently added it to Github and done this short write-up.

## Images

Images were obtained by parsing captions of from a large dataset (https://cocodataset.org/#download) with imageFinder.py then using imageResizer.py to manually crop and resize the images to 128 by 128 pixels.

## Network

The jupyter notebooks neural.ipynb and dnn.ipynb implement both the low-level forward and backward propagation steps required to train the network and the network itself, respectively. 