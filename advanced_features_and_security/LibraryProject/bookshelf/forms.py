from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn', 'summary']  # Adjust fields as per your model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add any custom field modifications here, such as adding widgets

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)