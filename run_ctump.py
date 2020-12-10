from ctump import Ctump

bot = Ctump()
# try:
#     for row in bot.check_diem_hoc_lai_cai_thien():
#         print(bot.get_diem(row['mssv'], row['mhp']))
# except:
#     pass
# bot.loc_danh_sach_hoc_lai_chua_duyet()
data = ["RH0403",
        "RH0404",
        "RH0501",
        "YT0201",
        "RH0310",
        "RH0311",
        "RH0109",
        "RH0110",
        "RH0610",
        "RH0611",
        "RH0508"
        ]
for item in data:
    bot.ds_sv_chua_chia_phong(item)
