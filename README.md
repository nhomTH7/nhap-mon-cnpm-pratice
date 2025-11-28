library = []   # Danh sách lưu trữ sách

# -------------------------------
# 1. Thêm sách
# -------------------------------
def add_book():
    print("\n--- Thêm sách mới ---")
    book_id = input("Nhập mã sách: ")
    title = input("Nhập tên sách: ")
    author = input("Nhập tác giả: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "status": "available"    # available = chưa mượn
    }

    library.append(book)
    print("✔ Thêm sách thành công!")


# -------------------------------
# 2. Hiển thị danh sách sách
# -------------------------------
def show_books():
    print("\n--- Danh sách sách ---")
    if len(library) == 0:
        print("Không có sách nào!")
        return

    for book in library:
        print(f"Mã: {book['id']} | Tên: {book['title']} | Tác giả: {book['author']} | Trạng thái: {book['status']}")


# -------------------------------
# 3. Tìm sách theo mã
# -------------------------------
def find_book():
    print("\n--- Tìm sách theo mã ---")
    search_id = input("Nhập mã sách cần tìm: ")

    for book in library:
        if book["id"] == search_id:
            print(f"✔ Đã tìm thấy: {book}")
            return
    print("✘ Không tìm thấy sách!")


# -------------------------------
# 4. Mượn sách
# -------------------------------
def borrow_book():
    print("\n--- Mượn sách ---")
    book_id = input("Nhập mã sách muốn mượn: ")

    for book in library:
        if book["id"] == book_id:
            if book["status"] == "available":
                book["status"] = "borrowed"
                print("✔ Mượn sách thành công!")
            else:
                print("✘ Sách đang được mượn!")
            return

    print("✘ Không tìm thấy mã sách!")


# -------------------------------
# 5. Trả sách
# -------------------------------
def return_book():
    print("\n--- Trả sách ---")
    book_id = input("Nhập mã sách muốn trả: ")

    for book in library:
        if book["id"] == book_id:
            if book["status"] == "borrowed":
                book["status"] = "available"
                print("✔ Trả sách thành công!")
            else:
                print("✘ Sách chưa được mượn!")
            return

    print("✘ Không tìm thấy mã sách!")


# -------------------------------
# 6. Menu chính
# -------------------------------
def menu():
    while True:
        print("\n====== QUẢN LÝ THƯ VIỆN ======")
        print("1. Thêm sách")
        print("2. Hiển thị sách")
        print("3. Tìm sách theo mã")
        print("4. Mượn sách")
        print("5. Trả sách")
        print("6. Thoát")
        
        choice = input("Chọn chức năng (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            find_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Tạm biệt!")
            break
        else:
            print("❗ Lựa chọn không hợp lệ! Vui lòng nhập 1-6.")




