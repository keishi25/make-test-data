from get_query import get_query


class OriginalData:
    """
        DBからの生データの取得
    """

    def __init__(self, cur, start_date, end_date):
        self.cur = cur
        self.start_date = start_date
        self.end_date = end_date

    def get_total_data(self):
        # 実績データ取得
        query = get_query('get_total_result.sql')
        self.cur.execute(query, start_date=self.start_date, end_date=self.end_date)
        data = self.cur.fetchall()

        return data


class ProcessData:

    def __init__(self, cur, start_date, end_date):
        self.cur = cur
        self.start_date = start_date
        self.end_date = end_date



if __name__ == "__main__":
    print(" ")
