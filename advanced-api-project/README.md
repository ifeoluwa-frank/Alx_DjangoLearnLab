# Advanced API Project

## API Endpoints

- **GET /books/**: List all books (public).
- **GET /books/<id>/**: Retrieve a single book by ID (public).
- **POST /books/create/**: Add a new book (authenticated users only).
- **PUT /books/<id>/update/**: Update an existing book (authenticated users only).
- **DELETE /books/<id>/delete/**: Delete a book (authenticated users only).

### Authentication

Use Django REST Framework's token-based authentication:
- Obtain a token via the `obtain-auth-token` endpoint.
- Include the token in the `Authorization` header for restricted endpoints:


## Permissions

- **Public Access**: `GET /books/` and `GET /books/<id>/`.
- **Authenticated Access**: All other endpoints.

## Features

- Custom validation in `BookCreateView` prevents duplicate book titles.
- Filtering by author ID in `BookListView` via query parameters.

