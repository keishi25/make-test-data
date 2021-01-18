from datetime import datetime as dt

sys.path.append('data')  # get_dataモジュールを呼ぶため
from connect_db import get_connect, end_connect, get_data
from get_data import OriginalData, StructureData

config_ini = configparser.ConfigParser()
config_ini.read('ini/config.ini', encoding='utf-8')

# connect db
mpasc1 = config_ini["DB_Info"]["aaaa"]
con, cur = get_connect(mpasc1)

