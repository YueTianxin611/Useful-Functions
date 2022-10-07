# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:36:20 2019

@author: 018614
"""

import copy
import pandas as pd

data = pd.read_csv('C:/Users/tianxin/Desktop/ML/parameter_control/data/testdata_2019_w_k.csv')


# 根据经验数据重构数据
def simple_variable_build(data, quantity, variable, row):
    """
    data:待重构的数据
    """
    data0 = copy.deepcopy(data).reset_index(drop=True)
    data1 = data0.iloc[row]
    data_out = pd.DataFrame(columns=data0.columns)
    value_list = []

    if len(set(data0[variable])) <= quantity:
        for i in set(data0[variable]):
            data1.loc[variable] = i
            data_out = data_out.append(data1)
            value_list.append(i)
        value_list.sort()
    else:
        unit = (max(data0[variable]) - min(data0[variable])) / quantity
        for i in range(0, quantity):
            data1.loc[variable] = min(data0[variable]) + i * unit
            data_out = data_out.append(data1)
            value_list.append(min(data0[variable]) + i * unit)

    return data_out, value_list


# 通过指定取值范围重组数据
def simple_variable_build_1(quantity, variable, max_value, min_value, features_list, values_list):
    """
        作用：
            ********************
        输入：
            quantity:希望指定变量的数量
            variable：指定变量
            max_value:指定变量可取的最大值
            min_value:指定变量可取的最小值
            features_list:填充变量list
            values_list：与features_list相对应的填充变量取值
        输出：
            True,dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe
    """

    columns = copy.deepcopy(features_list)
    list(columns).append(variable)
    data_out = pd.DataFrame(index=[1], columns=columns)
    for i in range(0, len(features_list)):
        data_out[features_list[i]] = list(values_list)[i]
    data1 = data_out.iloc[0]

    unit = (max_value - min_value) / (quantity - 1)
    for i in range(0, quantity):
        data1[variable] = min_value + i * unit
        data_out = data_out.append(data1)
    data_out = data_out.reset_index(drop=True).drop(0, axis=0)

    return data_out


# simple_variable_build_1(10,'MATERIAL_THICK',3,2,['WR_ROUGH','REDUC_RATIO','kcrough'],[1,23,4])

# 通过指定取值范围重组数据
# 连续型变量
def simple_variable_build_con(quantity, variable, max_value, min_value, **features):
    """
        作用：
            ********************
        输入：
            quantity:希望指定变量的数量
            variable：指定变量
            max_value:指定变量可取的最大值
            min_value:指定变量可取的最小值
            **features：其他填充变量
        输出：
            dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe
    """

    features[variable] = 0
    data_out = pd.DataFrame.from_dict(features, orient='index').T
    data1 = data_out.iloc[0]

    unit = (max_value - min_value) / (quantity - 1)
    for i in range(0, quantity):
        data1.loc[variable] = min_value + i * unit
        data_out = data_out.append(data1)
    data_out = data_out.reset_index(drop=True).drop(0, axis=0)
    print(data_out.shape)
    return data_out


# simple_variable_build_con(10,'MATERIAL_THICK',3,2,WR_ROUGH=1,REDUC_RATIO=23,kcrough=4)

# 通过指定取值重组数据
# 离散型变量
def simple_variable_build_dis(variable, value_list, **features):
    """
        作用：
            ********************
        输入：
            variable：指定变量
            value_list:指定变量可取的值
            **features：其他填充变量

        输出：
            dataframe: 处理成功，输出处理后数据，一般为pandas.dataframe
    """

    features[variable] = 0
    data_out = pd.DataFrame.from_dict(features, orient='index').T
    data1 = data_out.iloc[0]

    for value in value_list:
        data1.loc[variable] = value
        data_out = data_out.append(data1)
    data_out = data_out.reset_index(drop=True).drop(0, axis=0)
    return data_out

# simple_variable_build_dis('MATERIAL_THICK',[1,2,3],WR_ROUGH=1,REDUC_RATIO=23,kcrough=4)