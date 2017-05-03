
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[2]:

# load the data
fname = '/Users/pinqingkan/OneDrive/JobSearch/DataScience/PythonDataScience/DAT210x-master/Module3/Datasets/wheat.data'
X = pd.read_csv(fname, index_col = 0)


# In[3]:

X.columns


# In[5]:

# 3D scatter plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.set_xlabel('area')
# ax.set_ylabel('perimeter')
# ax.set_zlabel('asymmetry')
# ax.scatter(X.area, X.perimeter, X.asymmetry, c = 'red')
# plt.show()


# In[6]:

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(X.width, X.groove, X.length, c = 'green')
plt.show()


# In[ ]:



