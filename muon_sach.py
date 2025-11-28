# Danh sách sách trong thư viện (dạng list of dict)
thu_vien = [
    {"ma_sach": "S01", "ten": "Giáo dục học đại cương", "so_luong": 3},
    {"ma_sach": "S02", "ten": "Lý luận dạy học Tin học", "so_luong": 2},
    {"ma_sach": "S03", "ten": "Toán rời rạc", "so_luong": 1}
]

def muon_sach(ma_sach):
    # Tìm sách theo mã
    for sach in thu_vien:
        if sach["ma_sach"] == ma_sach:
            if sach["so_luong"] > 0:
                sach["so_luong"] -= 1
                print(f"Mượn thành công: {sach['ten']}")
                return
            else:
                print( "Sách này đã hết. Không thể mượn.")
                return
    print(" Không tìm thấy mã sách trong thư viện.")
print("=== HỆ THỐNG MƯỢN SÁCH THƯ VIỆN SƯ PHẠM ===")
ma = input("Nhập mã sách cần mượn (ví dụ: S01): ")
muon_sach(ma)

print(" Danh sách sách sau khi mượn:")
for s in thu_vien:
    print(f"{s['ma_sach']} - {s['ten']} - Còn lại: {s['so_luong']}")