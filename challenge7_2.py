# -*- coding:utf-8 -*-

import pandas as pd

def co2_gdp_plot():
    #读取世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='表名')
    
    # 1.查看数据文件结构
    # 2.选择 co2 和 GDP 数据
    # 3.针对缺失数据进行处理
    # 4.分国家计算数据总和
    # 5.归一化数据
    # 6.绘图

    # 绘图对象
    fig = plt.subplot()

    # 返回中国所对应的数据（归一化后，保留3位小数）
    china = [CO2数据,GDP数据]

    # 返回fig对象，以及中国对应的数据列表
    return fig,china
