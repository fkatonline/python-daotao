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

    def set_lich_tung_sinh_vien(self, mssv, mhp, gd, time):
        self.driver.find_element_by_name("txtSV").send_keys(mssv)
        self.driver.find_element_by_id("txtHP").send_keys(mhp)
        self.driver.find_element_by_name("Submit").click()
        self.driver.find_element_by_id("chkAll").click()
        self.driver.find_element_by_css_selector("#form1 > div:nth-child(4) > a:nth-child(3)").click()
        self.driver.find_element_by_name("txtPhongthi").send_keys(gd)
        self.driver.find_element_by_name("txtNgaygio").send_keys(time)
        self.driver.find_element_by_name("button1").click()
        sleep(1)

    def filter_by_mhp(self, mhp):
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        self.driver.find_element_by_id("txtHP").send_keys(mhp)
        self.driver.find_element_by_name("Submit").click()
        select = Select(self.driver.find_element_by_name('cboRPP'))
        select.select_by_value("500")
        self.driver.find_element_by_xpath("//*[contains(text(),'Trạng thái')]").click()

    def dong_tien(self, masv):
        self.driver.get("https://htql.ctump.edu.vn/ctump/dichvucong/admin/caithiendiem.php")
        self.driver.find_element_by_name("txtSV").send_keys(masv)
        self.driver.find_element_by_name("txtSV").send_keys(Keys.ENTER)

    def set_lich_mhp(self, mhp):
        self.filter_by_mhp(mhp)
        try:
            gio_phong_value = self.driver.find_element_by_xpath("//table/tbody/tr[2]/td[9]").text.rsplit("-", 1)
            gio_phong_key = ["time", "phong"]
            gio_phong_dict = dict(zip(gio_phong_key, gio_phong_value))
            print(gio_phong_dict)
        except:
            print(f"{mhp} khong co sinh vien thi cai thien")
            return
        self.driver.find_element_by_id("chkAll").click()
        self.driver.find_element_by_xpath("//*[contains(text(),'Lịch thi')]").click()
        self.driver.find_element_by_name("txtPhongthi").send_keys(gio_phong_dict['phong'])
        self.driver.find_element_by_name("txtNgaygio").send_keys(gio_phong_dict['time'])
