from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Model representing an author.
    - name: Stores the author's name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    - title: The book's title.
    - publication_year: The year the book was published.
    - author: Foreign key linking to the Author model.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title