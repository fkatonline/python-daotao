from time import sleep
from selenium import webdriver


class HoSoTuyenSinh:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://htql.ctump.edu.vn/ctump/tuyensinh/admin")
        self.driver.find_element_by_name('txtUsername').send_keys("admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin@123")
        self.driver.find_element_by_name('txtPassword').submit()

    def nhap(self, ma_ho_so):
        edit_button = "//a[contains(@href,'sua_hoso.php')]"
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get("https://htql.ctump.edu.vn/ctump/tuyensinh/admin/hoso.php")
        self.driver.find_element_by_id("maso").send_keys(ma_ho_so)
        self.driver.find_element_by_name("ewwe").submit()
        sleep(1)
        self.driver.find_element_by_xpath(edit_button).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


bot = HoSoTuyenSinh()
maso_raw = """

"""
list_of_maso = maso_raw.split()
for maso in list_of_maso:
    try:
        bot.nhap(maso)
    except:
        pass
bot.driver.switch_to.window(bot.driver.window_handles[1])
