Features:
CRUD operations for blog posts.
Authenticated users can create, edit, and delete their own posts.
Public can view the post list and details.
URLs:
/posts/ - List all posts.
/posts/new/ - Create a new post.
/posts/<int:pk>/ - View post details.
/posts/<int:pk>/edit/ - Edit a post.
/posts/<int:pk>/delete/ - Delete a post.
Permissions:
Only authors can edit/delete their posts.