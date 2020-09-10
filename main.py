from ctump import Ctump
from lich_thi_cai_thien import LichThi

# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()

raw_data = """YY0611
YT0305
YT0306
CB0501
YY0926
YY0902
CB0204
YT0417
YT0401
YY1006
YY0601
YY0602
YY0602
YY0607"""
data = set(raw_data.split())
bot = LichThi()
for d in data:
    # bot.set_lich_mhp(d)
    bot.filter_by_mhp(d)
