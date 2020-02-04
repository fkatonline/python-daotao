from diem import Diem
from lich_thi_cai_thien import LichThi

data_lich = [
    {
        "mahp":     "YY0312",
        "gd":       "02.KY",
        "thoigian": "17g30 05/2/2020"
    },
    {
        "mahp":     "YY1105",
        "gd":       "02.KY",
        "thoigian": "17g30 05/2/2020"
    },
    {
        "mahp":     "YY1105",
        "gd":       "02.KY",
        "thoigian": "17g30 05/2/2020"
    },
    {
        "mahp":     "YY0923",
        "gd":       "12.KY",
        "thoigian": "17g30 05/2/2020"
    },
    {
        "mahp":     "YY2007",
        "gd":       "12.KY",
        "thoigian": "17g30 05/2/2020"
    }
]
data_diem = [
        {
            "mssv": 1453010042,
            "mhp":  "YY2502"
        },
        {
            "mssv": 1553010505,
            "mhp":  "CB0111"
        },
        {
            "mssv": 1553030110,
            "mhp":  "DK0205"
        },
        {
            "mssv": 1553030110,
            "mhp":  "DK0403"
        },
        {
            "mssv": 1653030016,
            "mhp":  "DK0403"
        },
        {
            "mssv": 1653080031,
            "mhp":  "YY2525"
        },
        {
            "mssv": 1753030107,
            "mhp":  "YY0103"
        },
        {
            "mssv": 1753080035,
            "mhp":  "CB0403"
        },
        {
            "mssv": 1853011078,
            "mhp":  "YY0601"
        }
    ]

bot_lich = LichThi()
for item in data_lich:
    bot_lich.set_lich(item['mahp'], item['gd'], item['thoigian'])

bot_diem = Diem()
for item in data_diem:
    bot_diem.get_diem(item['mssv'], item['mhp'])
