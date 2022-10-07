import numpy as np
from math import pi as PI


def loadData(filename):
    file = open(filename)
    lines = file.readlines()
    data = []
    for line in lines[1:]:
        d = line.strip().split('\t')
        d = d[1:]
        data.append(d)
    return np.array(data)


# 所有计算采用拉普拉斯修正，朴素贝叶斯分类
# 计算先验概率
def calcpro(data):
    data_count = len(data)
    s_l = set(data[:, -1])
    N = len(s_l)
    yes_count = 0
    for vec in data:
        if vec[-1] == '是':
            yes_count += 1
    return (yes_count + 1) / (data_count + N)


# 用于计算标签的条件概率
def calcLabelpro(data, i, value):
    data_yes_len = 0
    fec_yes = 0
    fec_no = 0
    s_f = set(data[:, i])
    Ni = len(s_f)
    for vec in data:
        if vec[-1] == '是':
            data_yes_len += 1
        if vec[i] == value:
            if vec[-1] == '是':
                fec_yes += 1
            else:
                fec_no += 1
    # print(fec_yes,fec_no,data_yes_len)
    return (fec_yes + 1) / (data_yes_len + Ni), (fec_no + 1) / (len(data) - data_yes_len + Ni)


# 高斯概率密度
def gass(x, u, d):
    pro = (2 * PI) ** 0.5 * d ** 0.5
    pro = 1 / pro
    pro = pro * np.exp(-(x - u) ** 2 / (2 * d))
    return pro


# 用于计算连续数值的概率密度
def calcNumpro(data, i, value):
    data_yes = []
    data_no = []
    for vec in data:
        if vec[-1] == '是':
            data_yes.append(vec[i])
        else:
            data_no.append(vec[i])

    num_yes = list(map(float, data_yes))
    num_no = list(map(float, data_no))
    num_yes = np.array(num_yes)
    num_no = np.array(num_no)
    # print(num_yes.mean(),num_yes.var()**0.5)
    # 计算均值与方差
    mean_yes = num_yes.mean()
    var_yes = num_yes.var()
    mean_no = num_no.mean()
    var_no = num_no.var()

    pro_yes = gass(value, mean_yes, var_yes)
    pro_no = gass(value, mean_no, var_no)

    return pro_yes, pro_no


def Bayes(train_data, test_data):
    # 获得先验概率
    pro_yes = calcpro(train_data)
    pro_no = 1 - pro_yes
    for i in range(len(test_data) - 1):
        if i < 6:
            py, pn = calcLabelpro(data, i, test_data[i])
            pro_yes = pro_yes * py
            pro_no = pro_no * pn
        else:
            py, pn = calcNumpro(data, i, float(test_data[i]))
            pro_yes = pro_yes * py
            pro_no = pro_no * pn
    if pro_yes > pro_no:
        print('是')
    else:
        print('否')
    print(test_data[-1])


# AODE分类器，未实现连续属性(使用每个属性作为超父来构建SPODE)
# 首先计算P(C,Xi)
def calcP_C_Xi(data, i, value):
    D = len(data)
    label_set = set(data[:, -1])
    N = len(label_set)
    i_set = set(data[:, i])
    Ni = len(i_set)
    Xi_yes_count = 0
    Xi_no_count = 0
    for vec in data:
        if vec[i] == value:
            if vec[-1] == '是':
                Xi_yes_count += 1
            else:
                Xi_no_count += 1
    P_y = (Xi_yes_count + 1) / (D + N * Ni)
    P_n = (Xi_no_count + 1) / (D + N * Ni)
    return P_y, P_n


# 其次计算P(Xj|C,Xi)
def calcP_Xj_C_Xi(data, j, i, value_j, value):
    j_set = set(data[:, j])
    Nj = len(j_set)
    Xi_y_count = 0
    Xi_n_count = 0
    Xij_y_count = 0
    Xij_n_count = 0
    for vec in data:
        if vec[i] == value:
            if vec[-1] == '是':
                Xi_y_count += 1
            else:
                Xi_n_count += 1
            if vec[j] == value_j:
                if vec[-1] == '是':
                    Xij_y_count += 1
                else:
                    Xij_n_count += 1
    p_y = (Xij_y_count + 1) / (Xi_y_count + Nj)
    p_n = (Xij_n_count + 1) / (Xi_n_count + Nj)
    return p_y, p_n


def AODE(train_data, test_data):
    p_y_list = []
    p_n_list = []
    p_y = 1
    p_n = 1
    for i in range(6):
        P_c_Xi_y, P_c_Xi_n = calcP_C_Xi(data, i, test_data[i])
        for j in range(6):
            P_c_Xji_y, P_c_Xji_n = calcP_Xj_C_Xi(data, j, i, test_data[j], test_data[i])
            p_y = p_y * P_c_Xji_y
            p_n = p_n * P_c_Xji_n
        p_y_list.append(p_y * P_c_Xi_y)
        p_n_list.append(p_n * P_c_Xi_n)
    if sum(p_y_list) > sum(p_n_list):
        print('是')
    else:
        print('否')
    print(test_data[-1])


if __name__ == '__main__':
    data = loadData('C:/Users/tianxin/Desktop/ML/waterwatermelon/AODE.txt')
    test_data = ['乌黑', '蜷缩', '沉闷', '稍糊', '稍凹', '硬滑', '0.666', '0.091']
    Bayes(data, test_data)
    AODE(data, test_data)

