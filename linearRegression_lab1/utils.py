import numpy as np

def load_data():
    data = np.loadtxt("/home/buddha-thapa-magar/Documents/machine learning/sourceCode/lab1/exp1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("/home/buddha-thapa-magar/Documents/machine learning/sourceCode/lab1/exp2data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y
