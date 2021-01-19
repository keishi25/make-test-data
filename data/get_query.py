import os


def get_query(file_name):
    dir_path = '/data/sql/insert/'
    path = os.getcwd() + dir_path+ file_name
    with open(path, 'r', encoding='sjis') as f:
        query = f.read()
        return query


