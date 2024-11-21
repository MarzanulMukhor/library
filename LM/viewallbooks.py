def view_all_books(all_books):
      if all_books != []:
          for book in all_books:
              print(f"Title : {book['title']} | Author {book['author']} | ISBN :{book['isbn']} | Year :{book['year']}")
      else:
          print("No books found in all Books File")
