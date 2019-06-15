import numpy as np
import re
import math
# for clasification the group of database
f = open('data.txt', 'r')#read data file
def cosfuntion(X,theta,Y):
  #print(theta);
  m = np.max(X.shape)
  cost = (-1/(2*m))*np.sum(np.square(X.transpose().dot(theta) - Y))
  tmptheta = theta
  tmptheta[0] = 0
  tmptheta = theta - 0.000001*(X.dot(X.transpose().dot(theta) - Y))/m - 0.3*tmptheta/m
  #tmptheta[1] = theta[1] - 0.000001*(X[1].dot(X.transpose().dot(theta) - Y))/m
  theta = tmptheta
  
  print('cost value', "    ", cost)
  return theta
def optimize(X, theta , Y,iner):
  for i in range(iner):
    theta = cosfuntion(X, theta, Y)
  print(theta)
def load_data():
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
[X,Y] = load_data()
theta = np.array([[3],[1]])
print(X.shape, Y.shape, theta.shape)
optimize(X,theta,Y,1000)