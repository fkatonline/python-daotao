from selenium import webdriver
import pandas as pd
from secret import USERNAME, PASSWORD


class Diem():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.find_element_by_id("quanly").click()
        self.driver.find_element_by_class_name("selected").find_element_by_id("txt_Login_ten_dang_nhap").send_keys(
            USERNAME)
        self.driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").send_keys(PASSWORD)
        self.driver.find_element_by_class_name("selected").find_element_by_id("pw_Login_mat_khau").submit()

    def get_diem(self, mssv, mhp):
        self.driver.get("https://htql.ctump.edu.vn/quanly/diem/xemdiemtoankhoasinhvien")
        self.driver.find_element_by_id("txt_sr_index_ma_sinh_vien").send_keys(mssv)
        self.driver.find_element_by_id("cmb_s_sr_index").click()
        self.driver.find_element_by_id("rd_xemdiemtoankhoasinhvien_chon_0").click()
        self.driver.find_element_by_id("txt_sr_mhsv_ma_mon_hoc").send_keys(mhp)
        self.driver.find_element_by_id("cmb_s_sr_mhsv").click()
        data_html = self.driver.find_element_by_id("tb_xemdiemtoankhoasinhvien_diemtoankhoa").get_attribute("outerHTML")
        df = pd.read_html(data_html)[0]

        try:
            diem_list = [float(number) for number in df["Điểm HP tổng hợp"]]
        except:
            pass
        diem_info_dict = {"mssv": mssv, "mhp": mhp, "diem": diem_list}
        return diem_info_dict
