from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import admin_view, librarian_view, member_view



urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),  # URL for adding a book
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),  # URL for editing a book
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'), 
]
