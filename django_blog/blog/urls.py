from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("posts/", PostListView.as_view(), name="post-list"),  # List all posts
    path("post/new/", PostCreateView.as_view(), name="post-create"),  # Create a new post
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),  # View post details
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),  # Update a post
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),  # Delete a post
]
