# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def co2_gdp_plot():
    #读取世界银行气候变化数据集
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    #df_country = pd.read_excel("ClimateChange.xlsx",sheetname='Country')
    
    # 1.查看数据文件结构
    
    # 2.选择 co2 和 GDP 数据
    df_co2 = df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_gdp = df_climate[df_climate['Series code']=='NY.GDP.MKTP.CD']
    # 去掉不相关数据并且设置 Country code 为索引列
    df_co2_1 = df_co2.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code')
    df_gdp_1 = df_gdp.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1).set_index('Country code')
    
    # 替换确实数据单元 .. 为 NaN
    df_co2_replace = df_co2_1.replace({'..':pd.np.NaN})
    df_gdp_replace = df_gdp_1.replace({'..':pd.np.NaN})
    
    # 3.针对缺失数据进行处理
    # 填充空白数据
    df_co2_fill = df_co2_replace.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)
    df_gdp_fill = df_gdp_replace.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)
    
    # 去掉填充后仍然空白的数据
    df_co2_fill.dropna(how='all',inplace=True)
    df_gdp_fill.dropna(how='all',inplace=True)
    
    # 4.分国家计算数据总和
    df_co2_fill['total'] = df_co2_fill.apply(lambda x:x.sum(),axis=1)
    df_gdp_fill['total'] = df_gdp_fill.apply(lambda x:x.sum(),axis=1)
    
    # 5.归一化数据
    xc_max = df_co2_fill['total'].max()
    xc_min = df_co2_fill['total'].min()
    df_co2_fill['CO2-SUM'] = df_co2_fill['total'].apply(lambda x:round((x-xc_min)/(xc_max-xc_min),3))
    
    xg_max = df_gdp_fill['total'].max()
    xg_min = df_gdp_fill['total'].min()
    df_gdp_fill['GDP-SUM'] = df_gdp_fill['total'].apply(lambda x:round((x-xg_min)/(xg_max-xg_min),3))

    #df_coun = df_country.drop(['Capital city','Region','Income group'],axis=1).set_index('Country code')
        
    #df_co2_comb = pd.merge(df_coun,df_co2_fill,left_index=True,right_index=True)
    #df_gdp_comb = pd.merge(df_coun,df_gdp_fill,left_index=True,right_index=True)
    
    # 将两列归一化后的数据组合到一个DataFrame中
    df_comb = pd.concat([df_co2_fill['CO2-SUM'],df_gdp_fill['GDP-SUM']],axis=1)
    #print(df_co2_comb.head(10))
    #print(df_gdp_comb.head(10))
    #print(df_comb.head(20))
    
    #print(df_comb[df_comb.index == 'CHN'][['CO2-SUM','GDP-SUM']])
    # 获取中国的CO2 ，GDP数据
    china_df = df_comb[df_comb.index == 'CHN']
    china = [float(china_df['CO2-SUM']),float(china_df['GDP-SUM'])]
    print('CHINA :\n %s'%china)

    # 6.绘图

    # 绘图对象
    # ？？此处对于横坐标存在疑问，以及xticks的用法
    countries_labels=['USA','CHN','FRA','RUS','GBR']

    sticks_labels = []

    labels_position = []

    for i in range(len(df_comb)):
        if df_comb.index[i] in countries_labels:
            sticks_labels.append(df_comb.index[i])
            labels_position.append(i)
    
    fig = plt.subplot()
    df_comb.plot(
            kind='line',
            title='GDP-CO2',
            ax=fig
            )
    plt.xlabel('Countries')
    plt.ylabel('Values')

    plt.xticks(labels_position,sticks_labels,rotation='vertical')
    plt.show()

    # 返回中国所对应的数据（归一化后，保留3位小数）
    #china = [CO2数据,GDP数据]

    # 返回fig对象，以及中国对应的数据列表
    return fig,china

if __name__ == '__main__':
    co2_gdp_plot()
