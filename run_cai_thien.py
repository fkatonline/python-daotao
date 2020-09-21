from lich_thi_cai_thien import LichThi

# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()

raw_data = """YY0312
CB0205
YY1907
DD0205
YY0402
CB0405
YY1716
YY1716
YY1009"""
bot = LichThi()
# data = raw_data.split()
# for d in data:
#     # bot.set_lich_mhp(d)
#     bot.filter_by_mhp(d)
bot.dong_tien(1653010173)

