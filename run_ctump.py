from ctump import Ctump

bot = Ctump()
data =[
  {
    "mssv": 1733070052,
    "mhp": "YY1117"
  },

]
try:
    for row in data:
        print(bot.get_diem(row["mssv"], row["mhp"]))
except:
    pass
