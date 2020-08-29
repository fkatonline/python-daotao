from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret import user_name, password


class LichThi:
    def __init__(self):
        self.driver = webdriver.Firefox()
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
# bot.dong_tien(1653040075)

data = [
    {
        "mssv": 1753010007,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010067,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010075,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010184,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010188,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010190,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010259,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010266,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010277,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010284,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010329,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010332,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010364,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010380,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010386,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010388,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010419,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010477,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010498,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010524,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010529,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010532,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010572,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010600,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010629,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010630,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010639,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010662,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010669,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010679,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010724,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010754,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010760,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010771,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010774,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010779,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010780,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010783,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010790,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010831,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010859,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010860,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010870,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010897,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010908,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010910,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010911,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010914,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010925,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010942,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010943,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010948,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010971,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010972,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753010984,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011002,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011018,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011024,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011031,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011047,
        "mahp": "YY0501",
        "gd": "10.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011058,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011064,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011090,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011109,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011111,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011115,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011128,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011132,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011134,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011139,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011153,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011164,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011174,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753011179,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1753040048,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1853050041,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1853050066,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    },
    {
        "mssv": 1853050109,
        "mahp": "YY0501",
        "gd": "11.KY",
        "thoi_gian": "17g30-31-08-2020"
    }
]
bot = LichThi()
for item in data:
    bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
    print(item)
