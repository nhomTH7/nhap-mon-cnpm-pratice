def check_book(book, library):
    return book in library

lib = ["Python", "Cấu trúc dữ liệu", "Giải thuật"]

print(check_book("Python", lib))
print(check_book("Toán rời rạc", lib))
