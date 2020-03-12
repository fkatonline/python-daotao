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
    "YY2101",
    "YT0108",
    "YY2511",
    "YT0003",
    "YY2539",
    "YY2545",
    "RH0410",
    "YY1607",
]
bot.check_lich_thi(data)
