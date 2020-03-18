from time import sleep

from diem import Diem
from lich_thi_cai_thien import LichThi

# data_diem = []
# bot_diem = Diem()
# for item in data_diem:
#     print(bot_diem.get_diem(item['mssv'], item['mhp']))
#
#
# bot_diem.driver.close()

# data = []
#
# bot = LichThi()
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(item)

bot = LichThi()
data = [
    "YY2401",
    "YY0803",
    "YY0801",
    "DK0209",
    "CB0102",
    "YY1123",
    "YY0933",
    "YY0934",
    "YY0807",
    "RH0207",
    "DK0301",
    "DK0301",
    "CB0201",
    "DD0401",
    "YY2537",
]
bot.check_lich_thi(data)
