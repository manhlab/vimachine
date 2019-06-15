import numpy as np 
# thamso y = 3x + 4
f= open("data.txt","a+")
def data(iner, epsilon):
  X = np.ones((iner,1))
  Y = np.zeros((iner,1))
  for i in range(1,iner):
    X[i] = i + epsilon*np.random.randn()
    Y[i] = 3*X[i] + 4 + epsilon*np.random.randn()
    f.write(str(str(X[i])+"  "+ str(Y[i])+ '\n'))
    print(X[i],"  ", Y[i])
  f.close()
data(1000,0.2)