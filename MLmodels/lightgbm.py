import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import train_test_split


# 打开csv
df = open(r'','rb')
data_in = pd.read_csv(df)

# 加载数据
data_var = data_in['']
target = data_in['']
data = np.array(data_var)
target = np.array(target)

# 划分训练集测试集
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.3)
lgb_train = lgb.Dataset(X_train, y_train)
lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)

# 模型参数
param = {
    'max_depth': 10,
    'num_leaves': 18,
    'learning_rate': 0.05,
    'scale_pos_weight': 1,
    'num_threads': 8,
    'objective': 'regression',
    'bagging_fraction': 0.9,# 每次迭代时用的数据比例
    'bagging_freq': 1,
    'min_sum_hessian_in_leaf': 0.001
}
param['is_unbalance'] = 'true'
# param['metric'] = 'quantile'
param['metric'] = 'auc'


# 开始训练
print('Start training...')

gbm = lgb.train(param,
                lgb_train,
                num_boost_round=500,
                valid_sets=lgb_eval,
                )

y_predict = gbm.predict(X_test)


# 误差描述
def des_error(data_error):
    print("标准查差是", data_error.std())
    print("误差差均值是", data_error.mean())
    print('----------------------------------------------------')
    data_error_abs = np.abs(data_error)
    print("最大误差", data_error_abs.max())
    print("平均误差", data_error_abs.mean())
    return None


ori_error = (y_predict - y_test) / (y_test + X_test[:, -1])
des_error(ori_error)


# 保存model
# joblib.dump(gbm,'model_2.m')
# 载入模型
# gbm = joblib.load('clf.m')

