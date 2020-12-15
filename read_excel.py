import pandas as pd

df = pd.read_excel(r"C:\Users\Fkat\Desktop\danh sach mon hoc lien thong hk2.xls", index_col=None, header=None)
text_to_drop = [
    'Trường Đại học Y Dược Cần Thơ',
    'BỘ Y TẾ',
    'Danh Sách Kế Hoạch Giảng Dạy Và Học Phần',
    'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',
    'Độc lập - Tự do - Hạnh phúc'
]
print(df[~df.isin(text_to_drop)])
