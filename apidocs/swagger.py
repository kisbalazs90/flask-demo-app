# swagger_annotations.py

swagger_config = {
    "title": "Book API",
    "description": "API documentation for Book Management",
    "version": "1.0",
    "uiversion": 3,
    "authorizations": {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "JWT Bearer token authentication"
        }
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "JWT Bearer token"
        }
    },
    "security": [{"Bearer": []}],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/{}.json'.format('apispec_1'),
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "headers": [],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}


LOGIN_ANNOTATION =      """
    User Login
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "admin"
            password:
              type: string
              example: "admin"
    responses:
      200:
        description: Successfully authenticated
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
      401:
        description: Invalid credentials
        schema:
          type: object
          properties:
            msg:
              type: string
              example: "Bad username or password"
    """

GET_BOOKS_ANNOTATION = """
Get a list of all books
---
responses:
  200:
    description: A list of books
security:
  - Bearer: []
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
security:
  - Bearer: []
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
security:
  - Bearer: []
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
security:
  - Bearer: []
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
security:
  - Bearer: []
"""