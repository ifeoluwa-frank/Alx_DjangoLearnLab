from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Check if the user has the 'Member' role
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})