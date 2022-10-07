import pandas as pd


# 载入数据
data_in = pd.read_csv('')
# 划分训练集测试集
X_train = data_in['']
y_train = data_in['']
X_test = data_in['']
y_test = data_in['']

# 回归模型
from sklearn.linear_model import LinearRegression  #线性回归
mod_LR = LinearRegression()

from sklearn import tree
mod_DTR = tree.DecisionTreeRegressor()

from sklearn import ensemble
mod_RFR = ensemble.RandomForestRegressor(n_estimators=20)

from sklearn import ensemble
mod_ABR = ensemble.AdaBoostRegressor(n_estimators=50)

# 模型选择
mod = mod_DTR

# 模型训练
model = mod.fit(X_train, y_train)

# 模型预测
y_pred = mod.predict(X_test)

# feature importance
feature_importance_list = model.feature_importances_
