size_disket = 1.44 * 1024 * 1024
size_i = 4
symbols_in_string = 25
strings_in_list = 50
list_in_book = 100
count_of_books = int(size_disket // (size_i * symbols_in_string * strings_in_list * list_in_book))

print("Количество книг, помещающихся на дискету:", count_of_books)
