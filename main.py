from ctump import Ctump
from lich_thi_cai_thien import LichThi

# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()


data = [
    {
        "mssv": 1453010090,
        "mhp":  "CB0304"
    },
    {
        "mssv": 1553011059,
        "mhp":  "YT0501"
    },
    {
        "mssv": 1553011059,
        "mhp":  "YY0411"
    },
    {
        "mssv": 1553011059,
        "mhp":  "YY0501"
    },
    {
        "mssv": 1553011059,
        "mhp":  "YY0924"
    },
    {
        "mssv": 1553011059,
        "mhp":  "YY1801"
    },
    {
        "mssv": 1653010966,
        "mhp":  "YY1104"
    },
    {
        "mssv": 1653010966,
        "mhp":  "YY1602"
    },
    {
        "mssv": 1753020022,
        "mhp":  "CB0303"
    },
    {
        "mssv": 1753070057,
        "mhp":  "YY0708"
    },
    {
        "mssv": 1753070057,
        "mhp":  "YY1006"
    },
    {
        "mssv": 1853010260,
        "mhp":  "YY0402"
    },
    {
        "mssv": 1853010260,
        "mhp":  "YY0701"
    },
    {
        "mssv": 1853060014,
        "mhp":  "CB0301"
    }
]
bot = Ctump()
for d in data:
    print(bot.get_diem(d['mssv'], d['mhp']))
