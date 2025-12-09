# quanlybandoc.py

readers = []   # danh sách bạn đọc


# =============================
def them_ban_doc():
    print("\n=== THÊM BẠN ĐỌC MỚI ===")

    ma_doc = input("Mã bạn đọc: ")
    ten = input("Họ và tên: ")
    ngay_sinh = input("Ngày sinh (dd/mm/yyyy): ")
    dia_chi = input("Địa chỉ: ")
    sdt = input("Số điện thoại: ")
    email = input("Email: ")

    ban_doc = {
        "ma_doc": ma_doc,
        "ten": ten,
        "ngay_sinh": ngay_sinh,
        "dia_chi": dia_chi,
        "sdt": sdt,
        "email": email
    }

    readers.append(ban_doc)
    print(">> Đã thêm bạn đọc thành công!")