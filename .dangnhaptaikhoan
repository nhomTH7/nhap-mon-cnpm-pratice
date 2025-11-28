# Danh sách tài khoản sinh viên (mssv: mật khẩu)
accounts = {
    "SV001": "123456",
    "SV002": "abc123",
    "SV003": "password"
}

def login():
    print("=== HỆ THỐNG ĐĂNG NHẬP THƯ VIỆN ===")
    attempts = 3

    while attempts > 0:
        mssv = input("Nhập mã số sinh viên: ").strip()
        password = input("Nhập mật khẩu: ").strip()

        if mssv in accounts and accounts[mssv] == password:
            print(">> Đăng nhập thành công! Chào sinh viên", mssv)
            return True
        else:
            attempts -= 1
            print("Sai thông tin. Bạn còn", attempts, "lần thử.\n")

    print(">> Tài khoản bị khóa tạm thời. Vui lòng thử lại sau.")
    return False

# Chạy chương trình
login()
