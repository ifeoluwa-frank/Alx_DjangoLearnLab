from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    
    def setUp(self):
        """
        Set up test data for Book and Author models
        """
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Sorcerer's Stone",
            publication_year=1997,
            author=self.author
        )
        self.user = User.objects.create_user(username='testuser', password='password')
        self.url = '/api/books_all/'  # Adjust the URL if needed
    
    def test_create_book(self):
        """
        Test creating a book via the API
        """
        data = {
            'title': 'New Book Title',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Ensure one new book was created
        self.assertEqual(Book.objects.latest('id').title, 'New Book Title')

    def test_update_book(self):
        """
        Test updating a book's details via the API
        """
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2000,
            'author': self.author.id
        }
        response = self.client.put(f"{self.url}{self.book.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh the book instance from the database
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book(self):
        """
        Test deleting a book via the API
        """
        response = self.client.delete(f"{self.url}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Book should be deleted
    
    def test_get_book_list(self):
        """
        Test retrieving a list of books
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One book exists in the database
    
    def test_get_book_detail(self):
        """
        Test retrieving a single book's details
        """
        response = self.client.get(f"{self.url}{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter and the Sorcerer\'s Stone')

    def test_permissions(self):
        """
        Test that permissions are enforced correctly
        """
        # Test that an unauthenticated user can't create a book
        data = {
            'title': 'Unauthenticated Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authenticate the user and try creating the book again
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_filter_books(self):
        """
        Test filtering books based on title and publication_year
        """
        Book.objects.create(title="The Casual Vacancy", publication_year=2012, author=self.author)
        response = self.client.get(self.url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # One book with "Harry Potter" in the title
    
    def test_search_books(self):
        """
        Test searching for books by title and author
        """
        response = self.client.get(self.url, {'search': 'Rowling'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # The book by J.K. Rowling should match the search
    
    def test_order_books(self):
        """
        Test ordering books by publication year
        """
        Book.objects.create(title="The Ickabog", publication_year=2020, author=self.author)
        response = self.client.get(self.url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)  # First book in order should be the earliest one

