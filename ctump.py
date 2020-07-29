from time import sleep

from selenium import webdriver
import pandas as pd
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from secret import USERNAME, PASSWORD


class Ctump:
    def __init__(self):
        # options = Options()
        # options.headless = True
        # self.driver = webdriver.Firefox(options=options)
        self.driver = webdriver.Firefox()
        self.driver.get("https://htql.ctump.edu.vn/quanly")
        self.driver.find_element_by_id("quanly").click()
        self.driver.find_element_by_class_name("selected") \
            .find_element_by_id("txt_Login_ten_dang_nhap").send_keys(USERNAME)
        self.driver.find_element_by_class_name("selected") \
            .find_element_by_id("pw_Login_mat_khau").send_keys(PASSWORD)
        self.driver.find_element_by_class_name("selected") \
            .find_element_by_id("pw_Login_mat_khau").submit()

    def get_diem(self, mssv, mhp):
        self.driver.get("https://htql.ctump.edu.vn/quanly/diem/xemdiemtoankhoasinhvien")
        self.driver.find_element_by_id("txt_sr_index_ma_sinh_vien").send_keys(mssv)
        self.driver.find_element_by_id("cmb_s_sr_index").click()
        self.driver.find_element_by_id("rd_xemdiemtoankhoasinhvien_chon_0").click()
        self.driver.find_element_by_id("txt_sr_mhsv_ma_mon_hoc").send_keys(mhp)
        self.driver.find_element_by_id("cmb_s_sr_mhsv").click()
        data_html = self.driver.find_element_by_id("tb_xemdiemtoankhoasinhvien_diemtoankhoa").get_attribute("outerHTML")
        df = pd.read_html(data_html)[0]
        diem_list = [number for number in df["Điểm HP tổng hợp"]]
        return {"mssv": mssv, "mhp": mhp, "diem": diem_list}

    def xoa_chua_dong_tien(self, mssv):
        url = "https://htql.ctump.edu.vn/quanly/dangkyhocphan/qlsvdangkyhoclai"
        for m in mssv:
            self.driver.execute_script("window.open('','_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(url)
            sleep(1)
            self.driver.find_element_by_id("txt_sr_frm_ma_sinh_vien").send_keys(m)
            self.driver.find_element_by_id("cmb_s_sr_frm").click()
            try:
                self.driver.find_element_by_id("chk_qlsvdangkyhoclai_check_all").click()
                self.driver.find_element_by_id("btnDelete").click()
                self.driver.switch_to.alert.accept()
            except:
                pass
    def xoa_diem(self,data):
        for d in data:
            self.driver.get("https://htql.ctump.edu.vn/quanly/diem/nhapdiemhocphan")
            sleep(2)
            self.driver.find_element_by_id("txt_sr_index_ma_mon_hoc").send_keys(d["mahp"])
            self.driver.find_element_by_id("cmb_s_sr_index").click()
            self.driver.find_element_by_id("rd_list_nhap_0").click()
            self.driver.find_element_by_id("btNhapHP").click()
            try:
                self.driver.find_element_by_id("txt_sr_dsdsv_ma_sinh_vien").send_keys(d["mssv"])
                self.driver.find_element_by_id("cmb_s_sr_dsdsv").click()
                cac_cot_diem = self.driver.find_elements_by_xpath("//input[contains(@name,'txt_list')]")
                for c in cac_cot_diem:
                    c.clear()
                self.driver.find_element_by_id("btThucHien").click()
            except:
                pass