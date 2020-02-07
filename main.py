from time import sleep

from diem import Diem
from lich_thi_cai_thien import LichThi



data_diem = []
bot_diem = Diem()
for item in data_diem:
    print(bot_diem.get_diem(item['mssv'], item['mhp']))


bot_diem.driver.close()

# data = []
#
# bot = LichThi()
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(item)
