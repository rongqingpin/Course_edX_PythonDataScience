
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
# import matplotlib
import datetime


# In[2]:

from mpl_toolkits.mplot3d import Axes3D
from plyfile import PlyData, PlyElement


# In[3]:

# Load up the scanned 3D plot
flc = '/Users/pinqingkan/OneDrive/JobSearch/DataScience/PythonDataScience/DAT210x-master/Module4/Datasets/'
fname = flc + 'stanford_armadillo.ply'
X = PlyData.read(fname)


# In[4]:

# format as dataframe & reduce the No. of grids
reduce_factor = 1
Y = pd.DataFrame({
  'x':X['vertex']['z'][::reduce_factor],
  'y':X['vertex']['x'][::reduce_factor],
  'z':X['vertex']['y'][::reduce_factor]
})


# In[8]:

# Render the Original Armadillo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('Armadillo 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(Y.x, Y.y, Y.z, c='green', marker='.', alpha=0.75)
plt.show()


# In[ ]:



