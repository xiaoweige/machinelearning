Description

This section provides a brief introduction to the Perceptron algorithm
and the Sonar dataset to which we will later apply it.

Perceptron Algorithm
The Perceptron is inspired by the information processing of a single neural cell called a neuron.

A neuron accepts input signals via its dendrites, which pass the electrical signal down to the cell body.

In a similar way, the Perceptron receives input signals from examples of training data that we weight
and combined in a linear equation called the activation.
activation = sum(weight_i * x_i) + bias
The activation is then transformed into an output value or prediction using a transfer function,
such as the step transfer function.
prediction = 1.0 if activation >= 0.0 else 0.0
In this way, the Perceptron is a classification algorithm for problems
with two classes (0 and 1) where a linear equation (like or hyperplane)
can be used to separate the two classes.

It is closely related to linear regression and logistic regression
that make predictions in a similar way (e.g. a weighted sum of inputs).

The weights of the Perceptron algorithm must be estimated
from your training data using stochastic gradient descent.
Stochastic Gradient Descent
Gradient Descent is the process of minimizing a function by following the gradients of the cost function.

This involves knowing the form of the cost as well as the derivative so that
from a given point you know the gradient and can move in that direction,
e.g. downhill towards the minimum value.

In machine learning, we can use a technique that evaluates
and updates the weights every iteration called stochastic gradient descent
to minimize the error of a model on our training data.

The way this optimization algorithm works is that each training instance
is shown to the model one at a time. The model makes a prediction for a training instance,
the error is calculated and the model is updated in order to reduce the error for the next prediction.

This procedure can be used to find the set of weights in a model
that result in the smallest error for the model on the training data.

For the Perceptron algorithm, each iteration the weights (w) are
updated using the equation:
w = w + learning_rate * (expected - predicted) * x
Where w is weight being optimized, learning_rate is a learning rate
that you must configure (e.g. 0.01), (expected – predicted)
is the prediction error for the model on the training data
attributed to the weight and x is the input value.
Sonar Dataset
The dataset we will use in this tutorial is the Sonar dataset.

This is a dataset that describes sonar chirp returns bouncing
off different services. The 60 input variables are the strength
of the returns at different angles. It is a binary classification
problem that requires a model to differentiate rocks from metal cylinders.

It is a well-understood dataset. All of the variables are
continuous and generally in the range of 0 to 1. As such
we will not have to normalize the input data, which is
often a good practice with the Perceptron algorithm.
The output variable is a string “M” for mine and “R” 
for rock, which will need to be converted to integers 1 and 0.

By predicting the class with the most observations in
the dataset (M or mines) the Zero Rule Algorithm can achieve an accuracy of 53%.

You can learn more about this dataset at the UCI Machine Learning repository.
You can download the dataset for free and place it
in your working directory with the filename sonar.all-data.csv.
