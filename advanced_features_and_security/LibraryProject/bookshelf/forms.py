from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn', 'summary']  # Adjust fields as per your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add any custom field modifications here, such as adding widgets
