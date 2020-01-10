"""
The current code given is for the Assignment 1.
You will be expected to use this to make trees for:
> discrete input, discrete output
> real input, real output
> real input, discrete output
> discrete input, real output
"""

import numpy as np
import pandas as import pd
import matplotlib.pyplot as plt
from utils import entropy, information_gain, gini_index

class DecisionTree():
    def __init__(criterion):
        """
        Put all infromation to initialize your tree here.
        
        Example: Max Depth = 4
        """
        pass

    def fit(X, y):
        """
        Function to train and construct the decision tree
        Inputs:
        X: pd.DataFrame with rows as samples and columns as features (shape of X is N X P) where N is the number of samples and P is the number of columns. 
        y: pd.Series with rows corresponding to output variable (shape of Y is N)
        """
        pass

    def predict(X):
        """
        Funtion to run the decision tree on a data point
        """
        pass

    def plot():
        """
        Function to plot the tree
        
        Example:
        ?(X1 > 4)
            Y: ?(X2 > 7)
                Y: Class A
                N: Class B
            N: Class C
        Where Y => Yes and N => No
        """
        pass