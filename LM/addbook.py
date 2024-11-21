from savebook import save_all_books

def add_books(all_books):
    title = input("Enter Book Title : ")
    author = input("Enter Author Name : ")
    isbn = input("Enter ISBN Number : ")
    year = input("Enter Year : ")
    prize = int(input("Enter Prize : "))
    quantity = int(input("Enter Quantity : "))

    book = {
        "title"    : title,
        "author"   : author,
        "isbn"     : isbn,
        "year"     : year,
        "prize"    : prize,
        "quantity" : quantity,

    }
    all_books.append(book)
    save_all_books(all_books)

    print("Books added successfully")

    return all_books
