from ctump import Ctump

bot = Ctump()
# try:
#     for row in bot.check_diem_hoc_lai_cai_thien():
#         print(bot.get_diem(row['mssv'], row['mhp']))
# except:
#     pass
# bot.loc_danh_sach_hoc_lai_chua_duyet()

# data = """yy0201
# yy0101
# """.split()
# for item in data:
#     bot.ds_sv_chua_chia_phong(item)

# bot.duyet_khht()
bot.ds_sv_chua_chia_phong('yy0101')
