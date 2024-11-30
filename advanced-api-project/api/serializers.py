from rest_framework import serializers
from .models import Book, Author
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    - Includes validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - Includes nested serialization for books related to the author.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
