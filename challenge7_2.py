# -*- coding:utf-8 -*-

import pandas as pd

def co2_gdp_plot():
    #��ȡ������������仯���ݼ�
    df_climate = pd.read_excel("ClimateChange.xlsx",sheetname='����')
    
    # 1.�鿴�����ļ��ṹ
    # 2.ѡ�� co2 �� GDP ����
    # 3.���ȱʧ���ݽ��д���
    # 4.�ֹ��Ҽ��������ܺ�
    # 5.��һ������
    # 6.��ͼ

    # ��ͼ����
    fig = plt.subplot()

    # �����й�����Ӧ�����ݣ���һ���󣬱���3λС����
    china = [CO2����,GDP����]

    # ����fig�����Լ��й���Ӧ�������б�
    return fig,china
