import pandas as pd

# 载入数据
data_in = pd.read_csv('')
# 划分训练集测试集
X_train = data_in['']
y_train = data_in['']
X_test = data_in['']
y_test = data_in['']

# 分类模型
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier()

from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier()

from sklearn.ensemble import ExtraTreesClassifier
ETC = ExtraTreesClassifier()

# 模型选择
clf = RFC

# 模型训练
model = clf.fit(X_train, y_train)

# 模型预测
y_pred = clf.predict(X_test)

