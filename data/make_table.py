from get_query import get_query
from itertools import groupby
from operator import itemgetter
import os
import copy


class MakeTable:
    """
    DB tableの作成
    """
    def __init__(self, cur):
        self.cur = cur

    @staticmethod
    def make_sql_file(table_list):

        # グループIDでブルーピング
        table_list = sorted(table_list, key=itemgetter(3))
        for (key, recode) in groupby(table_list, key=itemgetter(3)):

            CREATE_TABLE_STR = "CREATE TABLE"
            table_name = key
            SPACE = " "
            COMMA = ","
            FRONT_BRACKET = "("
            BACK_BRACKET = ")"
            INDENTION = "\n"
            file_path = "data/sql/insert/"
            sql_file = table_name + ".sql"

            file = open(file_path + sql_file, 'w')
            file.write(CREATE_TABLE_STR)
            file.write(INDENTION)
            file.write(table_name)
            file.write(INDENTION)
            file.write(FRONT_BRACKET)
            file.write(INDENTION)

            # recode数カウント用
            recode_copy = copy.deepcopy(recode)
            recode_count = len(list(recode_copy))

            for index, element in enumerate(recode):
                file.write(element[0])  # カラム名
                file.write(SPACE)
                file.write(element[1])  # 属性
                if element[1] != "DATE":  # DATE型の時は、引数ナシ
                    file.write(FRONT_BRACKET)
                    file.write(str(element[2]))  # 桁数
                    file.write(BACK_BRACKET)

                # 最後はカンマなし
                if index != recode_count - 1:
                    file.write(COMMA)

                file.write(INDENTION)
            file.write(BACK_BRACKET)

            file.close()
        return None

    def execute(self):
        file_path = "data/sql/insert/"
        sql_file_list = os.listdir(file_path)
        for file in sql_file_list:
            query = get_query(file)
            self.cur.execute(query)

        return None
