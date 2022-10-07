# 常用 sklearn.decomposition.PCA
# 样本过多：IncrementalPCA
# 使用了L1正则化：SparsePCA和MiniBatchSparsePCA

# PCA类基本不需要调参，一般来说，我们只需要指定我们需要降维到的维度，
# 或者我们希望降维后的主成分的方差和占原始维度所有特征方差和的比例阈值就可以了

# explained_variance：代表降维后的各主成分的方差值。方差值越大，则说明越是重要的主成分
# explained_variance_ratio：代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的主成分

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.datasets.samples_generator import make_blobs
# X为样本特征，Y为样本簇类别， 共1000个样本，每个样本3个特征，共4个簇
X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3,3, 3], [0,0,0], [1,1,1], [2,2,2]], cluster_std=[0.2, 0.1, 0.2, 0.2],
                  random_state =9)
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X[:, 0], X[:, 1], X[:, 2],marker='o')
plt.show()


# 先不降维，只对数据进行投影，看看投影后的三个维度的方差分布
pca = PCA(n_components=3)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)

# 进行降维，从三维降到2维
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
# 看看此时转化后的数据分布
X_new = pca.transform(X)
plt.scatter(X_new[:, 0], X_new[:, 1],marker='o')
plt.show()

# 看不直接指定降维的维度，而指定降维后的主成分方差和比例
# 指定了主成分至少占95%
pca = PCA(n_components=0.95)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)

# MLE算法自己选择降维维度的效果
pca = PCA(n_components='mle')
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)

