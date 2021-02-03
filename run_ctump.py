from ctump import Ctump

bot = Ctump()
# try:
#     for row in bot.check_diem_hoc_lai_cai_thien():
#         print(bot.get_diem(row['mssv'], row['mhp']))
# except:
#     pass
# bot.loc_danh_sach_hoc_lai_chua_duyet()

data = """1453010234
1653010025
1653010025
1653010417
1853070033
""".split()
data1 = [
  {
    "mssv": 1453020039,
    "mhp": "RH0108"
  },
  {
    "mssv": 1653080121,
    "mhp": "YY0801"
  },
  {
    "mssv": 1753070057,
    "mhp": "YY0404"
  }
]
for item in data1:
    print(bot.get_diem(item['mssv'], item['mhp']))
