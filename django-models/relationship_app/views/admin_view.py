from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})