from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library


# Create your views here.
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to use for rendering
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books associated with this library to the context
        context['books'] = self.object.books.all()
        return context