import numpy as np
import pandas as pd
import matplotlib as plot
import re
import math
f = open('data.txt', 'r')
def sigmoid(X):
  #X.dtype = float64
  X = 1/ (1 + math.e^(-X))
  return X
def costFuntion(X, y ,theta):
  m = np.max(X.shape)
  cost = (-1/m)*(y*math.log( sigmoid(X.dot(theta)) - y)+ 
    (1-y)*math.log(sigmoid(1-X.dot(theta)) - y))
  tmptheta = theta
  tmptheta[0] = 0
  tmptheta = theta - (sigmoid(X.dot(theta)) - y).dot(X)
  theta = tmptheta
  print(cost)
  return theta
def optimize(X,Y,theta,iner):
  for i in range(iner):
    theta = costFuntion(X,Y, theta)
  return theta
def getdata():
  lines = f.readlines()
  X = np.ones((2,len(lines)))
  Y = np.ones((len(lines),1))
  count = 0
  for line in lines:
    tmp = line.split("  ")
    X[1][count] = re.sub('[^0-9,.]','', tmp[0])
    X[0][count] = 1
    Y[count][0] = re.sub('[^0-9,.]','', tmp[1])
    count = count + 1
  return [X,Y]  