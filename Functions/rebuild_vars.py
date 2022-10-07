import copy
import pandas as pd
import numpy as np
from functools import reduce
import matplotlib.pyplot as plt
data = pd.read_csv('')


# 通过指定取值范围重组数据
# 连续型变量
def build1(data, row, variable_list, feature_list, quantity_list, min_value_list, max_value_list):
    '''
    作用：
        根据用户输入的连续型变量取值范围重构数据
    输入：
        data:待重构的数据
        row:重构数据所在行数
        variable_list:指定变量
        feature_list:其他填充变量
        quantity_list:希望指定变量的数量
        min_value_list:指定变量可取的最小值
        max_value_list:指定变量可取的最大值
    输出：
        dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe

    '''
    unit_list = []
    for i in range(0, len(variable_list)):
        unit_list.append((max_value_list[i]-min_value_list[i])/(quantity_list[i]-1))
    columns = copy.deepcopy(feature_list)
    for i in range(0, len(variable_list)):
        columns.append(variable_list[i])
    n = 1
    for i in range(0,len(quantity_list)):
        n = n*quantity_list[i]
        n = int(n)
    m = []
    m.append(1)
    for i in range(1,len(variable_list)):
        m.append(m[i-1]*quantity_list[i-1])
    var_values = np.empty((len(variable_list), n))
    val_list = []
    for i in range(0,len(variable_list)):
        list1 = []
        for j in range(0, quantity_list[i]):
            v = min_value_list[i]+j*unit_list[i]
            list1.append(v)
        val_list.append(list1)
    fn = lambda x, code=',': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
    data0 = fn(val_list)
    for i in range(0, len(variable_list)):
        for j in range(0, n):
            var_values[i][j] = data0[j].split(",")[i]
    value_list = data.iloc[row][feature_list]
    data_out = pd.DataFrame(columns=feature_list, data=None)
    for i in range(0,len(variable_list)):
        data_out[variable_list[i]] = list(tuple(var_values[i]))
    for i in range(0,len(feature_list)):
        data_out[feature_list[i]] = value_list[i]
    data_out = data_out.reset_index(drop=True)
    return data_out
# build1(data,1,['v1','v2','v3','v4'],['WR_ROLLED_COUNT','WR_DIA'],[10,20,5,10],[1,3,5.5,6.6],[2,3.2,7.7,8.8])


# 通过指定取值范围重组数据
# 离散型变量
def build2(data, row, variable_list, var_value_list, feature_list):
    '''
    作用：
        根据用户输入的离散型变量取值范围重构数据
    输入：
        data:待重构的数据
        row:重构数据所在行数
        variable_list:指定变量
        var_value_list:指定变量的指定值
        feature_list:其他填充变量
    输出：
        dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe

    '''
    n = 1
    for i in range(0, len(var_value_list)):
        n = n*len(var_value_list[i])
        n = int(n)
    var_values = np.empty((len(variable_list), n))

    fn = lambda x, code=',': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
    data0 = fn(var_value_list)
    for i in range(0, len(variable_list)):
        for j in range(0, n):
            var_values[i][j] = data0[j].split(",")[i]
    value_list = data.iloc[row][feature_list]
    data_out = pd.DataFrame(columns=feature_list, data=None)
    for i in range(0,len(variable_list)):
        data_out[variable_list[i]] = list(tuple(var_values[i]))
    for i in range(0,len(feature_list)):
        data_out[feature_list[i]] = value_list[i]
    data_out = data_out.reset_index(drop=True)
    return data_out
# build2(data,1,['MEAS_STAND_SPD','MEAS_ENTHICK','MEAS_EXTHICK','MEAS_EXTENSION_STRESS'],[[1,2,3,4,5],[1,2,3,4,5],[1,2,3],[2,3,4]],['WR_ROLLED_COUNT','WR_DIA'])


# 根据经验数据重构数据
# 连续型变量
def build3(data,row,variable_list,feature_list,quantity_list):
    '''
    作用：
        根据经验值重构连续型数据
    输入：
        data:待重构的数据
        row:重构数据所在行数
        variable_list:指定变量
        feature_list:其他填充变量
        quantity_list:希望指定变量的数量
    输出：
        dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe

    '''
    min_value_list = []
    max_value_list = []
    for i in range(0,len(variable_list)):
        min_value_list.append(min(data[variable_list[i]]))
        max_value_list.append(max(data[variable_list[i]]))
    unit_list = []
    for i in range(0, len(variable_list)):
        unit_list.append((max_value_list[i]-min_value_list[i])/(quantity_list[i]-1))
    columns = copy.deepcopy(feature_list)
    for i in range(0, len(variable_list)):
        columns.append(variable_list[i])
    n = 1
    for i in range(0,len(quantity_list)):
        n = n*quantity_list[i]
        n = int(n)
    m = []
    m.append(1)
    for i in range(1,len(variable_list)):
        m.append(m[i-1]*quantity_list[i-1])
    var_values = np.empty((len(variable_list), n))
    val_list = []
    for i in range(0,len(variable_list)):
        list1 = []
        for j in range(0, quantity_list[i]):
            v = min_value_list[i]+j*unit_list[i]
            list1.append(v)
        val_list.append(list1)
    fn = lambda x, code=',': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
    data0 = fn(val_list)
    for i in range(0, len(variable_list)):
        for j in range(0, n):
            var_values[i][j] = data0[j].split(",")[i]
    value_list = data.iloc[row][feature_list]
    data_out = pd.DataFrame(columns=feature_list, data=None)
    for i in range(0,len(variable_list)):
        data_out[variable_list[i]] = list(tuple(var_values[i]))
    for i in range(0,len(feature_list)):
        data_out[feature_list[i]] = value_list[i]
    data_out = data_out.reset_index(drop=True)
    return data_out
# build3(data,1,['MEAS_STAND_SPD','MEAS_ENTHICK','MEAS_EXTHICK','MEAS_EXTENSION_STRESS'],['WR_ROLLED_COUNT','WR_DIA'],[10,20,5,10])


# 根据经验数据重构数据
# 离散型变量
def build4(data,row,variable_list,feature_list):
    '''
    作用：
        根据经验值重构离散型数据
    输入：
        data:待重构的数据
        row:重构数据所在行数
        variable_list:指定变量
        feature_list:其他填充变量
    输出：
        dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe

    '''
    var_value_list = []
    for i in range(0, len(variable_list)):
        list0 = data[variable_list[i]]
        list0 = set(list0)
        var_value_list.append(list0)
    n = 1
    for i in range(0,len(var_value_list)):
        n = n*len(var_value_list[i])
        n = int(n)
    var_values = np.empty((len(variable_list), n))

    fn = lambda x, code=',': reduce(lambda x, y: [str(i) + code + str(j) for i in x for j in y], x)
    data0 = fn(var_value_list)
    for i in range(0, len(variable_list)):
        for j in range(0, n):
            var_values[i][j] = data0[j].split(",")[i]
    value_list = data.iloc[row][feature_list]
    data_out = pd.DataFrame(columns=feature_list, data=None)
    for i in range(0,len(variable_list)):
        data_out[variable_list[i]] = list(tuple(var_values[i]))
    for i in range(0,len(feature_list)):
        data_out[feature_list[i]] = value_list[i]
    data_out = data_out.reset_index(drop=True)
    return data_out
# build4(data,1,['MEAS_STAND_SPD','MEAS_ENTHICK','MEAS_EXTHICK','MEAS_EXTENSION_STRESS'],['WR_ROLLED_COUNT','WR_DIA'])


def graph(data_out,variable_list,val):
    '''
    作用：
        绘制多个变量与目标变量的关系折线图
    输入：
        data_out:重构后的数据
        variable_list:希望绘制的变量
        val:目标值
    输出：
        一张图

    '''
    for i in range(0,len(variable_list)):
        x = data_out[variable_list[i]]
        plt.plot(x,val, marker='*')
        for x,y in zip(x,val):
            plt.text(x,y,y,fontsize=10)
    plt.show()
    plt.xlabel('variables')
    plt.ylabel('target value')
    plt.grid()
    return

