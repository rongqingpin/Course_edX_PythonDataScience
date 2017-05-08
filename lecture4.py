import pandas as pd
from sklearn.decomposition import PCA

# load data
fname = '/Users/pinqingkan/OneDrive/JobSearch/DataScience/PythonDataScience/DAT210x-master/Cached Datasets/students.data'
X = pd.read_csv(fname, index_col = 0)

# PCA
pca = PCA(n_components = 2, svd_solver = 'full')
pca.fit(X)
PCA(copy = True, n_components = 2, whiten = False)
Y = pca.transform(X)

print(X.shape)

print(Y.shape)