from rest_framework import generics, filters
from django_filters import rest_framework as django_filters  # Correct import for DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    - Supports filtering by 'title', 'author', and 'publication_year'.
    - Allows searching by 'title' and 'author'.
    - Results can be ordered by 'title' or 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Add filtering, searching, and ordering capabilities
    filter_backends = [
        django_filters.DjangoFilterBackend,  # For filtering
        filters.SearchFilter,  # For search functionality
        filters.OrderingFilter,  # For ordering
    ]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author']  # Fields for search functionality
    ordering_fields = ['title', 'publication_year']  # Fields for ordering


# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow read-only access for unauthenticated users

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict to authenticated users
