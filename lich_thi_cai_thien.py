from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret import user_name, password


class LichThi:
    def __init__(self):
        self.driver = webdriver.Chrome()
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


bot = LichThi()
bot.dong_tien(1853011033)

# data = [
#     {
#         "mssv": 1653040035,
#         "mahp": "YT0130",
#         "gd": "12.KY",
#         "thoi_gian": "17g30-31-08-2020"
#     }
# ]
# bot = LichThi()
# i = 1
# for item in data:
#     bot.set_lich_tung_sinh_vien(item['mssv'], item['mahp'], item['gd'], item['thoi_gian'])
#     print(i, end=' ')
#     print(item)
#     i = i + 1
# bot.driver.quit()
# data = [
#     "CB0303",
#     "CB0303",
#     "DK0501",
#     "DK0501",
#     "DK0408",
#     "YT0319",
#     "YT0503",
#     "DD0303",
#     "YY2525"
# ]
# bot.check_lich_thi(data)
