from django.urls import path
from .views import list_books, LibraryDetailView, CustomLoginView, CustomLogoutView, register

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
