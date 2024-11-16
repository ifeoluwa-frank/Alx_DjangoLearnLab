THIS IS MY INTRODUCTION TO DJANGO

## Permissions and Groups Setup

### Groups and Assigned Permissions
- **Editors**:
  - Can create, edit, and view books.
- **Viewers**:
  - Can only view books.
- **Admins**:
  - Full access: can create, edit, delete, and view books.

### How to Add Permissions
1. Add permissions in the `Book` model under `Meta`.
2. Assign permissions to groups in the Django admin interface.

### Enforcing Permissions
- Use `@permission_required` decorators in views to restrict actions.
- Example:
  ```python
  @permission_required('bookshelf.can_edit', raise_exception=True)
  def edit_book(request, pk):
      ...
