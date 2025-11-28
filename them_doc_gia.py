
danh_sach = ["Nhiên", "An", "Bình"]

ten_moi = input("Nhập tên cần thêm: ")

if ten_moi not in danh_sach:
    danh_sach.append(ten_moi)
    print("Đã thêm:", ten_moi)
else:
    print("Tên đã tồn tại trong danh sách!")

print("Danh sách:", danh_sach)
