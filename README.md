# Classifying Handwritten Digits
1. Using scikit-learn package in python to classify hand writting
2. Algorithms used including perceptron, support vectors machine(SVM), artificial neural networks (ANN)
3. Datasets are MINST(70,000 images of handwritten digits), Chars74k(74,000 images of digits 0-9, a-a)

## Perceptron
#### Introduction
 - An individual neuron can be thought of as a computational unit that processes one or more inputs to produce an output. 
 - A perceptron functions analogously to a neuron; it accepts one or more inputs, processes them, and returns an output.
 - It may seem that a model of just one of the hundreds of billions of neurons in the human brain will be of limited use. 
 - Perceptrons are capable of online, error-driven learning.
 - The learning algorithm can update the model's parameters using a single training instance rather than the entire batch of training instances. <br>
 <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/1.png" height = "120"/></br>
 - The circles labeled x1 , x2 , and x3 are inputs units.
 - Each input unit represents one feature. 
 - The circle in the center is a computational unit or the neuron's body. 
 - The edges connecting the input units to the computational unit are analogous to dendrites. Each edge is weighted.
 - The parameters can be interpreted easily.
 - The edge directed away from the computational unit returns the output and can be thought of as the axon.

#### Perceptron algorithms
 - The perceptron learning algorithm begins by setting the weights to zero or to small random values. 
 - Then predicts the class for a training instance. 
 - If the prediction is correct, the algorithm continues to the next instance. 
 - If the prediction is incorrect, the algorithm updates the weights.
<img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/2.png" height="30"/></br>
 - dj is the true class for instance j
 - y(t) is the predictedjclass for instance j
 - x is the value of the ith explanatory variable for instance j
 - α is a hyperparameter that controls the learning rate

#### Limitations of perceptron
 - Linear models can only learn to approximate the functions for linearly separable datasets. 
 - The linear classifiers that we have examined find a hyperplane that separates the positive classes from the negative classes
 - If no hyperplane exists that can separate the classes, the problem is not linearly separable.

#### SVM kernels
 - The decision boundary equation: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/3.png" height = "30"/>
 - Predictions are made using function:<img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/4.png" height="30"/>
 - Change it to primal form:<img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/5.png" height="30"/>
 - Left plot is linearly inseparable, right plot is linearly separable after mapping to a higher-dimensional space
  <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/12.png" width="400"/>
 - Apply the mapping to the feature vectors <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/6.png" height = "68"/>
 - The dot product is sclar, no require for mapping once this scalar has been computed: this is kernel trick
 - Kernel function: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/7.png" height="30"/>
 - Example for two feature vectors and square transformation: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/9.png" height="35"/> 
 - Kernel: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/10.png" height="68"/>
 - An example of kernel:
  <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/11.png" height="150"/>
 - Polynomial kernel: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/15.png" height="30"/>
 - Sigmoid kernel: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/16.png" height="30"/>
 - Gaussian kernel: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/17.png" height="30"/>
 
#### Classifying characters
 - Partitioned into 60,000 training, 10,000 testing
 - MINST data: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/13.png" width="240"/>
 - Chars74k data: <img src="https://github.com/yetianpro/handwritten-digits-classification/blob/master/pic/14.png" width="240"/>


 
