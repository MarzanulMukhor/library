import addbook
import viewallbooks
all_books = []

while True:
    print("Welcome to Library Management System")
    print(" 1. Add Books")
    print(" 2. View All Books")
    print(" 0. Exit")

    menu = input("Select any number : ")

    if menu == "0":
        print("Thanks for using Library Management System")
        break

    elif menu == "1":
       all_books = addbook.add_books(all_books)

    elif menu == "2":
        viewallbooks. view_all_books(all_books)

    else :
        print("Choose a valid number")