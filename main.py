from ctump import Ctump
from lich_thi_cai_thien import LichThi

# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()


data = ["YY1801",
        "YT0420",
        "DD0355",
        "RH0603",
        "YY0103",
        "YY0101",
        "YY0917",
        "DK0112",
        "YY0104",
        "YY0104",
        "YY0102"]
bot = LichThi()
bot.check_lich_thi(data)
