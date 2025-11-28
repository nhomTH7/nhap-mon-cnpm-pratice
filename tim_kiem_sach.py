library = ["Python cơ bản", "Lập trình C++", "AI nhập môn", "Lịch sử Việt Nam"]

keyword = input("Nhập tên sách cần tìm: ").lower()

found = [book for book in library if keyword in book.lower()]

if found:
    print("Sách tìm thấy:")
    for b in found:
        print("-", b)
else:
    print("Không tìm thấy sách phù hợp.")
