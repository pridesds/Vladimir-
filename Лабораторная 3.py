# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44  # размер дискеты в Мб
pages_in_book = 100  # количество страниц в книге
lines_per_page = 50  # число строк на странице
symbols_per_line = 25  # количество символов в строке
bytes_per_symbol = 4  # для хранения кода одного символа нужно 4 байта

disk_size_bytes = disk_size_mb * 1024 * 1024 #Перевод мб в байты

book_size_bytes = pages_in_book * lines_per_page * symbols_per_line * bytes_per_symbol #Расчёт объёма книги в байтах

number_of_books = int(disk_size_bytes // book_size_bytes) #Расчёт кол-ва книг на дискете

print("Количество книг, помещающихся на дискету:",number_of_books)