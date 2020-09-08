from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

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
            select = Select(self.driver.find_element_by_name('cboRPP'))
            select.select_by_value("500")
            self.driver.find_element_by_xpath("//*[contains(text(),'Trạng thái')]").click()
            # da_dong_tien_xpath = self.driver.find_elements_by_xpath("//*[contains(text(),'Đã thu phí')]")
            # da_dong_tien = len(da_dong_tien_xpath)
            # print(f"{d}: {da_dong_tien}")

    def dong_tien(self, masv):
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        self.driver.find_element_by_name("txtSV").send_keys(masv)
        self.driver.find_element_by_name("txtSV").send_keys(Keys.ENTER)
