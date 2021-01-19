import pandas as pd
from itertools import groupby
import itertools
from operator import itemgetter
import datetime


class GetTableInfo:
    @staticmethod
    def get_data(*sheet_name_list, type_select, file_path):
        data_list = {}
        for sheet_name in sheet_name_list:
            # pandasからデータ取得
            df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=type_select)
            # pandasからdelivery_quantity生成
            tmp = {sheet_name: [[row[column] for column in df] for i, row in df.iterrows()]}
            data_list.update(tmp)

        return data_list

    @staticmethod
    def get_info(file_path, sheet_name, type_select):
        # pandasからデータ取得
        df = pd.read_excel(file_path, sheet_name=sheet_name, dtype=type_select)
        return df

    @staticmethod
    def get_list(df, *column_list):
        table_df = df[list(column_list)]
        table_info_list = table_df.values  # dataFrameからlist化
        return table_info_list

#if __name__ == "__main__":
    #print(a)




