from ctump import Ctump

bot = Ctump()
# try:
#     for row in bot.check_diem_hoc_lai_cai_thien():
#         print(bot.get_diem(row['mssv'], row['mhp']))
# except:
#     pass
# bot.loc_danh_sach_hoc_lai_chua_duyet()
data = """RH0002
YY0923
YY1201
YY1901
YY2101
YY2201
YY2301
YY2401
""".split()
for item in data:
    bot.ds_sv_chua_chia_phong(item)
