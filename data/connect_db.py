import os

import cx_Oracle


def get_data(cur, query):
    """
    Oracle DBからデータの参照を行う
    """
    cur.execute(query)
    out = cur.fetchall()
    return out


def get_connect(info):
    """
    oracle DBと接続を行う
    info = "【ユーザ名】/【パスワード】@【アドレス】:【ポート】/【サービスネーム】"
    """
    con = cx_Oracle.connect(info)
    cur = con.cursor()

    return con, cur


def end_connect(con, cur):
    """
    oracle DBとの接続を切る
    """
    con.commit()
    cur.close()
    con.close()


if __name__ == '__main__':
    """
    運用の際は、下記の手法を使用する
    sample inputは、設定ファイルから取得
    sql_queryはget_queryモジュールから取得
    """