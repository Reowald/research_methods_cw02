import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils import *
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.multiclass import unique_labels
from sklearn.metrics.pairwise import euclidean_distances

'''THIS FILE IS NOT WORKING CURRENTLY TAKEN DIRECTLY FROM A LAB SESSION FILE FOR DATA MINING - 
NEEDS TO BE CODED FOR OUR PROJECT'''

# read CSV file in dataframe
news_data = pd.read_csv('compression_info.csv')


x = news_data['Original Size (bytes)']
y = news_data['Compressed Size (bytes)']


class My1NN(BaseEstimator, ClassifierMixin):

    def __init__(self):
        pass

    def fit(self, X, y):
        # check the data is correctly formatted.
        X, y = check_X_y(X, y)

        # get the class labels.
        self.classes_ = unique_labels(y)

        self._X = X
        self._y = y

        # return classifier
        return self

    def predict(self, X):
        check_is_fitted(self)

        # check the data is valid.
        X = check_array(X)

        # get the index of closest sample to our data
        closest = np.argmin(euclidean_distances(X, self._X), axis=1)

        # return the labels based on the index.
        return self._y[closest]


my_1nn = My1NN()
my_1nn.fit(X_train, y_train);