from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret import user_name, password


class LichThi:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        self.driver.find_element_by_name("txtUsername").send_keys(user_name)
        element = self.driver.find_element_by_name("txtPassword")
        element.send_keys(password)
        sleep(0.5)
        element.send_keys(Keys.RETURN)
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")

    def set_lich_tung_sinh_vien(self, mssv, mahp, gd, thoi_gian):
        self.driver.find_element_by_name("txtSV").send_keys(mssv)
        self.driver.find_element_by_id("txtHP").send_keys(mahp)
        self.driver.find_element_by_name("Submit").click()
        self.driver.find_element_by_id("chkAll").click()
        self.driver.find_element_by_css_selector("#form1 > div:nth-child(4) > a:nth-child(3)").click()
        self.driver.find_element_by_name("txtPhongthi").send_keys(gd)
        self.driver.find_element_by_name("txtNgaygio").send_keys(thoi_gian)
        self.driver.find_element_by_name("button1").click()
        sleep(1)

    def check_lich_thi(self, data):
        url = "https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php"
        for d in data:
            self.driver.execute_script("window.open('','_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(url)
            self.driver.find_element_by_id("txtHP").send_keys(d)
            self.driver.find_element_by_name("Submit").click()

    def dong_tien(self, masv):
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        self.driver.find_element_by_name("txtSV").send_keys(masv)
        self.driver.find_element_by_name("txtSV").send_keys(Keys.ENTER)


# bot = LichThi()
#
# data = [
#   {
#     "mssv": 1753080101,
#     "mahp": "YY2546",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1733010333,
#     "mahp": "YY2201",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-15-09-20"
#   },
#   {
#     "mssv": 1733010403,
#     "mahp": "YY2201",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-15-09-20"
#   },
#   {
#     "mssv": 1733010426,
#     "mahp": "YY2201",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-15-09-20"
#   },
#   {
#     "mssv": 1753050026,
#     "mahp": "YY1907",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1753010193,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010365,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010452,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010476,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010586,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010955,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753010977,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753011038,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753011064,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753011095,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753011149,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753080097,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1753080102,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040030,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040031,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040050,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040057,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040059,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040084,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853040085,
#     "mahp": "YY1801",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1653080027,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080032,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080042,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080094,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080099,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080104,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080109,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080116,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1653080120,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080026,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080030,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080037,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080037,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080042,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080043,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080049,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080058,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080059,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080063,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080064,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080067,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1833080068,
#     "mahp": "YY1716",
#     "gd": "12.KY",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1753010489,
#     "mahp": "YY1123",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1753010728,
#     "mahp": "YY1123",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1753010844,
#     "mahp": "YY1123",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1753011048,
#     "mahp": "YY1123",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1753011181,
#     "mahp": "YY1123",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1833080058,
#     "mahp": "YY1115",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1833080064,
#     "mahp": "YY1115",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1833080067,
#     "mahp": "YY1115",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1833030023,
#     "mahp": "YY0936",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1753010771,
#     "mahp": "YY0926",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1753080012,
#     "mahp": "YY0926",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1753080024,
#     "mahp": "YY0926",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1753010618,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753010697,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753010728,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753010771,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753011078,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753011104,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753011137,
#     "mahp": "YY0924",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733010027,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733010367,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733010408,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733010421,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733010441,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1733080027,
#     "mahp": "YY0923",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1753040080,
#     "mahp": "YY0902",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010753,
#     "mahp": "YY0701",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1853010865,
#     "mahp": "YY0701",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1853010912,
#     "mahp": "YY0701",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010067,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1653010069,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1653010289,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1653010611,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1653010624,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1653010890,
#     "mahp": "YY0611",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853070156,
#     "mahp": "YY0607",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080014,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080046,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080071,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080085,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080085,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853080085,
#     "mahp": "YY0602",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010266,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010611,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010788,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010831,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010865,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010884,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010912,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010920,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010046,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010071,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010079,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010096,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010097,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010111,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010159,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010180,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010200,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1933010215,
#     "mahp": "YY0601",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853070182,
#     "mahp": "YY0502",
#     "gd": "07.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953070077,
#     "mahp": "YY0404",
#     "gd": "PM4.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010400,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010415,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010464,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010505,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010522,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010524,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010537,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010797,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010988,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011010,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011042,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011072,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011119,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011125,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011128,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011130,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011130,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011149,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853011160,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010075,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010079,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010086,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010096,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010111,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010168,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1933010217,
#     "mahp": "YY0403",
#     "gd": "PM3.DD",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010198,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010272,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010564,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010610,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010620,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010645,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010662,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010669,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010722,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010747,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010865,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010876,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010884,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853010897,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853020002,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853020027,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853020070,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853040019,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853040059,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853040064,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853040094,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853040096,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853080023,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853080070,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853080095,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1853080098,
#     "mahp": "YY0402",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1953070081,
#     "mahp": "YY0104",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1933010149,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1933010217,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010108,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010186,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010632,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010654,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953040042,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953040057,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953040095,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953080037,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953080062,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953080085,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953080102,
#     "mahp": "YY0102",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010383,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010541,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010544,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010694,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010909,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010917,
#     "mahp": "YY0101",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1853020011,
#     "mahp": "YT0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1853040096,
#     "mahp": "YT0401",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1733030025,
#     "mahp": "DK0520",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1733030028,
#     "mahp": "DK0520",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653030003,
#     "mahp": "DK0516",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653030033,
#     "mahp": "DK0516",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653030045,
#     "mahp": "DK0516",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653030058,
#     "mahp": "DK0516",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653030083,
#     "mahp": "DK0516",
#     "gd": "10.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010044,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010067,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010144,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010161,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010186,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010252,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010309,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010310,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010330,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010345,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010372,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010374,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010611,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010624,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010702,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010703,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010775,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010805,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010814,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010817,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010831,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010838,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010851,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010869,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010893,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010927,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010939,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010941,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010957,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010972,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1653010991,
#     "mahp": "DK0305",
#     "gd": "06.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1733030058,
#     "mahp": "DK0112",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-09-09-20"
#   },
#   {
#     "mssv": 1953010186,
#     "mahp": "CB0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1953010498,
#     "mahp": "CB0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1953010541,
#     "mahp": "CB0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1953010544,
#     "mahp": "CB0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1953010567,
#     "mahp": "CB0501",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-11-09-20"
#   },
#   {
#     "mssv": 1853010865,
#     "mahp": "CB0406",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1853040015,
#     "mahp": "CB0406",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953040130,
#     "mahp": "CB0405",
#     "gd": "PM4.DD",
#     "thoi_gian": "07g30-12-09-20"
#   },
#   {
#     "mssv": 1953030099,
#     "mahp": "CB0403",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1853010896,
#     "mahp": "CB0401",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1853011069,
#     "mahp": "CB0401",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-14-09-20"
#   },
#   {
#     "mssv": 1953010088,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010119,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010186,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010200,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010358,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010488,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010490,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010512,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010541,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010544,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010567,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010584,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010609,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010632,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010639,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010654,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010694,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010699,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010857,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953010869,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953040057,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953080037,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953080062,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953080093,
#     "mahp": "CB0302",
#     "gd": "11.KY",
#     "thoi_gian": "17g30-07-09-20"
#   },
#   {
#     "mssv": 1953080037,
#     "mahp": "CB0201",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1953080093,
#     "mahp": "CB0201",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-10-09-20"
#   },
#   {
#     "mssv": 1953010490,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953010512,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953010585,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953010632,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953010654,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953010780,
#     "mahp": "CB0111",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-08-09-20"
#   },
#   {
#     "mssv": 1953080083,
#     "mahp": "CB0110",
#     "gd": "12.KY",
#     "thoi_gian": "17g30-10-09-20"
#   }
# ]
# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()

