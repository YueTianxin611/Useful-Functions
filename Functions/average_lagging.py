import pandas as pd


data_in = pd.read_excel('')


# 构造样本集
def build_data_1(data):
    current = data['流量']
    data_1 = data.loc[:, ["图像参数1", "图像参数2", "图像参数3","图像参数4","图像参数5","图像参数6","图像参数7","图像参数8","图像参数9","图像参数10", \
                          '流量', '智能加药池出水浊度', "混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"]]
    return current,data_1


# 平滑
def average_all(data, time):
    time = int(time*20)
    var_list = data.columns
    average_all_ = pd.DataFrame(columns=var_list)
    for i in var_list:
        test_data_1 = data[i]
        average = []
        for j in range(time,len(test_data_1)):
            temp = test_data_1[j-time+1:j].mean()
            average.append(temp)
        average_all_[i] = average
    return average_all_


# 数据置后 每一行置后步数不同
def lagging(data):
    data_values = pd.DataFrame(
        columns=["图像参数1", "图像参数2", "图像参数3", "图像参数4", "图像参数5", "图像参数6", "图像参数7", "图像参数8", "图像参数9", "图像参数10",
                 "智能加药池出水浊度","混凝剂投加量（mg/L）","絮凝剂投加量（mg/L）"])
    for i in range(len(data)):
        index_2 = int(411.68*20*60/data['流量'][i]+i+1)
        if index_2 <= len(data):
            values = data.iloc[index_2:index_2+1]
            data_values = data_values.append(values)
        else:
            pass
    data_values.rename(columns={'智能加药池出水浊度': '当前出水浊度'}, inplace=True)
    data_values = data_values.reset_index(drop=True)
    data_values = data_values.drop(['流量'], axis=1)
    target = data[['智能加药池出水浊度']][:len(data_values)].reset_index(drop=True)
    lagging_ = pd.concat([data_values, target], axis=1)
    return lagging_


# 数据置后 每一行置后步数相同
def lagging_1(data, time):
    target = data[['混凝剂投加量（mg/L）','絮凝剂投加量（mg/L）','智能加药池出水浊度']][int(time*20):].reset_index(drop = True)
    data_var = data.iloc[:-int(time*20),:].reset_index(drop = True)
    data_var.rename(columns={'混凝剂投加量（mg/L）':'当前混凝剂投加量','絮凝剂投加量（mg/L）':'当前絮凝剂投加量','智能加药池出水浊度':'当前出水浊度'}, inplace = True)
    lagging_ = pd.concat([data_var, target], axis=1)
    return lagging_


def data_prepare(data):
    current,data_1 = build_data_1(data)
    average_all_ = average_all(data_1, 5)
    data_pre_ = lagging(average_all_)
    return data_pre_


data_pre = data_prepare(data_in)
