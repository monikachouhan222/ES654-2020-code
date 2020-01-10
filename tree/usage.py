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
from tree import DecisionTree

# Test case 1
# Real Input and Real Output

N = 30
P = 5
X = np.random.randn(N, P)
y = np.random.randn(N)

tree = DecisionTree()
tree.fit(pd.DataFrame(X), pd.Series(y))
tree.predict(pd.DataFrame(X))
tree.plot()

# Test case 2
# Real Input and Discrete Output

N = 