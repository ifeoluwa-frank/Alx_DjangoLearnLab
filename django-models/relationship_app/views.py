from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


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
    
# Login view using Django's built-in view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view using Django's built-in view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view using Django's built-in UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            return redirect('list_books')  # Redirect to any page, e.g., books list
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})