import sklearn as sk
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets

from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

def getversion():
    print 'numpy',np.__version__
    print 'scikit-learn',sk.__version__
    print 'matplotlib',matplotlib.__version__

if __name__ == '__main__':
    iris = datasets.load_iris()
    X_iris,y_iris = iris.data,iris.target
    print X_iris.shape,y_iris.shape
    print X_iris[0],y_iris[0]
    # Get dataset with only the first two attributes
    X, y = X_iris[:,:2], y_iris
    # Split the dataset into a trainig and a testing set
    # Test set will be the 25% taken randomly
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    print X_train.shape, y_train.shape
    # Standarize the features
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)

    X_test = scaler.transform(X_test)
