from time import sleep
import pandas as pd
from selenium.webdriver.support.select import Select

from secret import USERNAME, PASSWORD
from helium import *


class Ctump:
    def __init__(self):
        Config.implicit_wait_secs = 60
        self.driver = start_firefox("https://htql.ctump.edu.vn/quanly")
        click(S('#quanly'))
        write(USERNAME)
        press(TAB)
        write(PASSWORD)
        press(ENTER)

    def get_diem(self, mssv, mhp):
        self.xem_diem_toan_khoa_sinh_vien(mssv)
        write(mhp, into=S("@txt_sr_mhsv_ma_mon_hoc"))
        click(S("#cmb_s_sr_mhsv"))
        data_html = S("#tb_xemdiemtoankhoasinhvien_diemtoankhoa").web_element.get_attribute("outerHTML")
        df = pd.read_html(data_html)[0]
        df.drop(df.tail(1).index, inplace=True)
        nam_hoc_list = [number for number in df["Năm học"]]
        diem_list = [number for number in df["Điểm HP tổng hợp"]]
        return {"mssv": mssv, "mhp": mhp, "nam_hoc": nam_hoc_list, "diem": diem_list}

    def xoa_chua_dong_tien(self, mssv):
        url = "https://htql.ctump.edu.vn/quanly/dangkyhocphan/qlsvdangkyhoclai"
        for m in mssv:
            self.driver.execute_script("window.open('','_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(url)
            self.driver.find_element_by_id("txt_sr_frm_ma_sinh_vien").send_keys(m)
            self.driver.find_element_by_id("cmb_s_sr_frm").click()
            print(m)
            try:
                self.driver.find_element_by_id("chk_qlsvdangkyhoclai_check_all").click()
                self.driver.find_element_by_id("btnDelete").click()
                self.driver.switch_to.alert.accept()
            except:
                pass

    def xoa_diem(self, data):
        for d in data:
            self.driver.get("https://htql.ctump.edu.vn/quanly/diem/nhapdiemhocphan")
            self.driver.find_element_by_id("txt_sr_index_ma_mon_hoc").send_keys(d["mhp"])
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

    def loc_danh_sach_hoc_lai_chua_duyet(self):
        self.driver.get("https://htql.ctump.edu.vn/quanly/dangkyhocphan/qlsvdangkyhoclai")
        duoc_duyet = Select(self.driver.find_element_by_id("cmb_sr_frm_2"))
        duoc_duyet.select_by_value("dkhl_duoc_duyet")
        chua_duyet_dang_ky = Select(self.driver.find_element_by_id("cmba_sr_frm_dkhl_duoc_duyet"))
        chua_duyet_dang_ky.select_by_value("0")
        self.driver.find_element_by_id("cmb_s_sr_frm").click()

    def get_table_data(self, table_id):
        data_html = self.driver.find_element_by_id(table_id).get_attribute("outerHTML")
        df = pd.read_html(data_html)[0]
        df.drop(df.tail(1).index, inplace=True)
        return df

    def check_diem_hoc_lai_cai_thien(self, table_id="tb_qlsvdangkyhoclai"):
        self.loc_danh_sach_hoc_lai_chua_duyet()
        df = self.get_table_data(table_id)
        df = df[['Mã sinh viên', 'Mã học phần']]
        df.columns = ['mssv', 'mhp']
        data = df.to_dict('records')
        return data

    def xem_diem_toan_khoa_sinh_vien(self, mssv):
        url = "https://htql.ctump.edu.vn/quanly/diem/xemdiemtoankhoasinhvien"
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)
        self.driver.find_element_by_id("txt_sr_index_ma_sinh_vien").send_keys(mssv)
        click(Button("Tìm"))
        click(S("#rd_xemdiemtoankhoasinhvien_chon_0"))

    def ds_sv_chua_chia_phong(self, mhp):
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        go_to('https://htql.ctump.edu.vn/quanly/diem/danhsachhocphan')
        write(mhp)
        press(ENTER)
        click(S('@img_danhsachhocphan_chitiet'))
        select(r'DSSV đã chia phòng', r'DSSV chưa chia phòng')
        click(r'Tìm')

    def duyet_khht(self, mssv):
        # duyet ke hoach hoc tap cho YHDP46
        go_to("https://htql.ctump.edu.vn/quanly/kehoach/dslop")
        select = Select(self.driver.find_element_by_id('cmb_sr_ds_hoc_ky'))
        select.select_by_value('3')
        select = Select(self.driver.find_element_by_id('cmb_sr_3'))
        select.select_by_value('ten_lop')
        select = Select(self.driver.find_element_by_id('cmba_sr_ten_lop'))
        select.select_by_value('205304A')
        click("Tìm")
        click(S("#img_dslop_chon_0"))
        write(mssv, into=S("#txt_frm_search_ma_sinh_vien"))
        click("Tìm")
        click(S("#img_dssinhviencualop_kehoachHT_0"))
        click(S("#btnDuyet"))
        click("Các học phần trong năm học (2020-2021) - học kỳ (Hè)")
        click("Thực hiện")




