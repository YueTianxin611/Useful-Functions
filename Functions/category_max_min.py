import pandas as pd


# 载入数据
data_in = pd.read_excel(r'C:\Users\tianxinxin\Desktop\drug\data_raw\data-0907.xlsx')
data_in = pd.DataFrame(data=data_in)
data_in = data_in.dropna(how='any',axis=0)
variables = ['图像参数1',"图像参数2","图像参数3","图像参数4","图像参数5","图像参数6",
           "图像参数7","图像参数8","图像参数9","图像参数10","PH","温度","进水浊度",
           "电导率","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]
target = "智能加药池出水浊度"


# 确定features的最大最小区间和分类步数
def max_min_step(data, n):
    list_ = pd.DataFrame(columns=variables, index=['max', 'min','step'])
    for var in variables:
        list_[var][0] = max(data[var])
        list_[var][1] = min(data[var])
        list_[var][2] = (max(data[var]) - min(data[var])) / n
    return list_


# 确定feature所在区间
def feature_divide(data, data_max_min_step, n):
    for var in variables:
        for k in range(n+1):
            MAX = data_max_min_step[var]['min'] + (k + 1) * data_max_min_step[var]['step']
            MIN = data_max_min_step[var]['min'] + k * data_max_min_step[var]['step']
            sel = (data[var] < MAX) & (data[var] >= MIN)
            data[var][sel] = k
    data = pd.concat([data[variables], data[target]], axis=1)
    return data


# 合并类别相同的行
def group_data(data):
    def ab(data):
        return list(data.values)
    data = data.groupby(variables)[target].apply(ab)
    data = data.reset_index()
    return data


# 确定目标区间最大值、最小值、极差、样本数
def get_group_max_min(data):
    max_list = []
    min_list = []
    num_list = []
    diff_list = []
    for i in range(len(data)):
        max_list.append(max(data[target][i]))
        min_list.append(min(data[target][i]))
        num_list.append(len(data[target][i]))
    data['目标最小值'] = min_list
    data['目标最大值'] = max_list
    data['区间样本数'] = num_list
    for j in range(len(max_list)):
        diff_list.append(max_list[j]-min_list[j])
    data['样本极差'] = diff_list
    return data


# 总函数
def main_(data,n):
    '''
    输入：
    data: 要处理的数据
    n: 变量划分的区间数
    输出：
    data: 包含分类好的变量和目标变量的区间信息
    '''
    max_min_step_list = max_min_step(data, n)
    data_divide = feature_divide(data, max_min_step_list, n)
    res = group_data(data_divide)
    data = get_group_max_min(res)
    return data
# main_(data_in, 100)




