# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:48:04 2016

@author: Stud
"""
# Standalone simple linear regression example

from math import sqrt
from random import seed,randrange
from csv import reader
#Load A csv file
def load_csv(filename):
    dataset = list()
    with open(filename,'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset
#Convert string column to float
def str_column_to_float(dataset,column):
    for row in dataset:
        row[column] = float(row[column].strip())
#Split a dataset into a train and test set
def train_test_split(dataset,split):
    train = list()
    train_size = split * len(dataset)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy
#claculate the mean of a list of numbers
def mean(values):
    return sum(values)/float(len(values))
#the variance is the sum squared difference for each value from the mean 
#variance for a list of numbers can be calculated as
def variance(values,mean):
    return sum([(x - mean)**2 for x in values])
#dataset=[[1,1],[2,3],[4,3],[3,2],[5,5]]
#x =[row[0] for row in dataset]
#y =[row[1] for row in dataset]
mean_x,mean_y=mean(x),mean(y)
var_x,var_y=variance(x,mean_x),variance(y,mean_y)
print ('x stats:mean=%.3f variance=%.3f' %(mean_x,var_x))
print ('y stats:mean=%.3f variance=%.3f' %(mean_y,var_y))
#calculate covariance
def covariance(x,mean_x,y,mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x)* (y[i] - mean_y)
    return covar
covar = covariance(x,mean_x,y,mean_y)
print ('Covariance : %.3f'%(covar))
#estimate coeffcients
def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    x_mean,y_mean=mean(x),mean(y)
    b1= covariance(x,x_mean,y,y_mean)/variance(x,x_mean)
    b0=y_mean - b1*x_mean
    return [b0,b1]
#b0,b1 = coefficients(dataset)
print ('Coefficients:b0=%.3f,b1=%.3f'%(b0,b1))
#now we know how to estimate the coefficients, the next step is to use them.
def simple_linear_regression(train,test):
    predictions = list()
    b0,b1 = coefficients(train)
    for row in test:
        yhat = b0+b1*row[0]
        predictions.append(yhat)
    return predictions
#calculate root mean squared error
def rmse_metric(actual,predicted):
    sum_error=0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error +=(prediction_error**2)
    mean_error =sum_error/float(len(actual))
    return sqrt(mean_error)
#evaluate regression algorithm on training dataset
#def evaluate_algorithm(dataset,algorithm):
#    test_set = list()
#    for row in dataset:
#        row_copy =list(row)
#        row_copy[-1] =None
#        test_set.append(row_copy)
#    predicted = algorithm(dataset,test_set)
#    print(predicted)
#    actual = [row[-1] for row in dataset]
#    rmse  = rmse_metric(actual,predicted)
#    return rmse    
#rmse = evaluate_algorithm(dataset,simple_linear_regression)
#print('RMSE: %.3f' % (rmse))

#Evaluate an algorithm using a train/test split
def evaluate_algorithm(dataset,algorithm,split,*args):
    train,test = train_test_split(dataset,split)
    test_set = list()
    for row in test:
        row_copy = list(row)
        row_copy[-1]=None
        test_set.append(row_copy)
    predicted = algorithm(train,test_set,*args)
    actual = [row[-1] for row in test]
    rmse = rmse_metric(actual,predicted)
    return rmse
#Simple linear regression on insurance dataset
seed(1)
#Load and prepare data
filename = 'insurance.csv'
dataset = load_csv(filename)
for i in range(len(dataset[0])):
    str_column_to_float(dataset,i)
#evaluation algorithm
split = 0.6
rmse = evaluate_algorithm(dataset,simple_linear_regression,split)
print('rmse:%.3f'%(rmse))