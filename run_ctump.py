from ctump import Ctump

bot = Ctump()
# try:
#     for row in bot.check_diem_hoc_lai_cai_thien():
#         print(bot.get_diem(row['mssv'], row['mhp']))
# except:
#     pass
# bot.loc_danh_sach_hoc_lai_chua_duyet()

data = ["1453010030",
        "1453010038",
        "1453010042",
        "1453010090",
        "1453010234",
        "1453010250",
        "1453010258",
        "1453010301",
        "1453010306",
        "1453010316",
        "1453010349",
        "1453010362",
        "1453010426",
        "1453010547",
        "1453010548",
        "1453010562",
        "1453010569",
        "1453010633",
        "1453010721",
        "1453010795",
        "1453010837",
        "1453010888"
        ]
for sv in data:
    bot.xem_diem_toan_khoa_sinh_vien(sv)
