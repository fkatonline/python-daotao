from time import sleep
from selenium import webdriver


class HoSoTuyenSinh:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get("https://htql.ctump.edu.vn/ctump/tuyensinh/admin")
        self.driver.find_element_by_name('txtUsername').send_keys("admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin@123")
        self.driver.find_element_by_name('txtPassword').submit()

    def nhap(self, ma_ho_so):
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get("https://htql.ctump.edu.vn/ctump/tuyensinh/admin/hoso.php")
        self.driver.find_element_by_id("maso").send_keys(ma_ho_so)
        self.driver.find_element_by_name("ewwe").submit()
        sleep(1)
        self.driver.find_element_by_xpath("//a[contains(@href,'sua_hoso.php')]").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_id("dvht11").click()


bot = HoSoTuyenSinh()
list_of_maso = [286705, 827944, 177055, 578120, 518597, 277921]
for maso in list_of_maso:
    try:
        bot.nhap(maso)
    except:
        pass
