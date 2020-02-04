from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret import user_name, password


class LichThi():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        element = self.driver.find_element_by_name("txtUsername")
        element.send_keys(user_name)
        element = self.driver.find_element_by_name("txtPassword")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")

    def set_lich(self, mahp, gd, thoigian):
        sleep(3)
        self.driver.find_element_by_id("txtHP").send_keys(mahp)
        self.driver.find_element_by_name("Submit").click()
        self.driver.find_element_by_id("chkAll").click()
        self.driver.find_element_by_css_selector("#form1 > div:nth-child(4) > a:nth-child(3)").click()
        self.driver.find_element_by_name("txtPhongthi").send_keys(gd)
        self.driver.find_element_by_name("txtNgaygio").send_keys(thoigian)
        self.driver.find_element_by_name("button1").click()
