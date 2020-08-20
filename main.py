from time import sleep

from ctump import Ctump
from lich_thi_cai_thien import LichThi

# data_diem = []
# bot_diem = Diem()
# for item in data_diem:
#     print(bot_diem.get_diem(item['mssv'], item['mhp']))
#
#
# bot_diem.driver.close()

# data = []
#
# bot = LichThi()
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(item)

# bot = LichThi()
# data = [
# "YY1823",
# "YY1821",
# "YY1704",
# "YY1703",
# "YY1702",
# "YY1701",
# "YY1604",
# "YY1603",
# "YY1602",
# "YY1601",
# "YY1128",
# "YY1105",
# "YY1005",
# "YY0944",
# "YY0907",
# "YY0903",
# "YY0405",
# "YY0404",
# "YY0314",
# "YY0104",
# "YT0504",
# "RH0007",
# "DK0517",
# "DK0502",
# "DK0501",
# "CB0401",
# "CB0304",
# "CB0110"
# ]
# bot.check_lich_thi(data)

bot = Ctump()
data = [
    {
        "mssv": 1653010514,
        "mahp": "yt0321"
    },
]
bot.xoa_diem(data)
