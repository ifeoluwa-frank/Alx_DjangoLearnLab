from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from bookshelf.models import CustomUser




class BookAdmin(admin.ModelAdmin):
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters in the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality
    search_fields = ('title', 'author')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
admin.site.register(Book, BookAdmin)

