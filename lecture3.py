# take advantage of interactive plot viewer
# of sublime text

import matplotlib.pyplot as plt
import pandas as pd
# load data
fname = '/Users/pinqingkan/OneDrive/JobSearch/DataScience/PythonDataScience/DAT210x-master/Cached Datasets/students.data'
X = pd.read_csv(fname, index_col = 0)
# 3D scatter plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('First Grade')
ax.set_ylabel('Final Grade')
ax.set_zlabel('Daily Alcohol')
ax.scatter(X.G1, X.G3, X.Dalc)

plt.show()