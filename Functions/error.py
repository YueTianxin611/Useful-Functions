import numpy as np
import matplotlib as plt
from sklearn.model_selection import KFold, cross_val_score
X_train = []
y_train = []
X_test = []
y_test = []
y_pred = []


# 误差描述
def des_error(data_error):
    print("标准查差是", data_error.std())
    print("误差差均值是", data_error.mean())
    print('----------------------------------------------------')
    data_error_abs = np.abs(data_error)
    print("最大误差", data_error_abs.max())
    print("平均误差", data_error_abs.mean())
    return None


from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error
# 分类准确率分数（指所有分类正确的百分比）
accuracy_score(y_pred, y_test)
# 平均绝对误差
mean_absolute_error(y_test, y_pred)
# 均方误差
mean_squared_error(y_test,y_pred)


# 误差图
def draw_error(data_error, fig):
    plt.figure(2 * fig)
    plt.hist(data_error, bins=500)
    plt.xlabel("origin Error")
    _ = plt.ylabel("Count")

    plt.figure(2 * fig + 1)
    data_error_abs = np.abs(data_error)
    plt.hist(data_error_abs, bins=500)
    plt.xlabel("origin Error")
    _ = plt.ylabel("Count")
    plt.show()
    return None


# 交叉验证
def cross_error(model):
    scores = cross_val_score(
             model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
    return scores,scores.mean()


# kFold 交叉验证
def rmsle_cv(model,n_folds):
    kf = KFold(n_folds, shuffle=True, random_state=42).get_n_splits(X_train.values)
    rmse= np.sqrt(-cross_val_score(model, X_train.values, y_train, scoring="neg_mean_squared_error", cv = kf))
    return(rmse)

