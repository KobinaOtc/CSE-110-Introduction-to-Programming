# Print all the books by using the with statment to ope and view the content of the file
with open('books.txt') as books:
    for book in books:
        book = book.strip()
        print(book)