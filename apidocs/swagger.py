# swagger_annotations.py


GET_BOOKS_ANNOTATION = """
Get a list of all books
---
responses:
  200:
    description: A list of books
"""

POST_BOOK_ANNOTATION = """
Add a new book
---
parameters:
  - name: body
    in: body
    required: true
    schema:
      type: object
      properties:
        title:
          type: string
        author:
          type: string
        published_year:
          type: integer
responses:
  201:
    description: Book created successfully
"""

GET_BOOKS_BY_ID_ANNOTATION = """
Get a book by ID
---
parameters:
  - name: book_id
    in: path
    required: true
    type: integer
responses:
  200:
    description: Book found
  404:
    description: Book not found
"""

UPDATE_BOOK_ANNOTATION = """
Update a book by ID
---
parameters:
  - name: book_id
    in: path
    required: true
    type: integer
  - name: body
    in: body
    required: true
    schema:
      type: object
      properties:
        title:
          type: string
        author:
          type: string
        published_year:
          type: integer
responses:
  200:
    description: Book updated successfully
  404:
    description: Book not found
"""

DELETE_BOOK_ANNOTATION = """Delete a book by ID
---
parameters:
  - name: book_id
    in: path
    required: true
    type: integer
responses:
  200:
    description: Book deleted successfully
  404:
    description: Book not found
"""