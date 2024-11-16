# Command:
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

# Expected Output:
<Book: 1984 by George Orwell (1949)>
