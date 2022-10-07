import pandas as pd


def data_joint(data_list):
    data_all = pd.DataFrame(columns = data_list[0].columns)
    for i in data_list:
        data_all = data_all.append(i,ignore_index=True)
    return data_all

#data_joint([data_10,data_11,data_12,data_13])