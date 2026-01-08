Django Blog Writing Platform

A clean, structured, and practical blog writing platform built with Django.
This project demonstrates real-world backend development practices by combining traditional Django template-based views with RESTful APIs using Django REST Framework.

This repository represents disciplined learning translated into working, deployable software.

.....Features.....
Web Application Features (HTML Views)
User authentication (login & logout)
Create, edit, and delete blog posts
Category-based post organization and filtering
Comment system for blog posts
Admin panel for managing posts, categories, comments, and users
Secure CSRF-protected forms
Clean and minimal UI using Django templates

.....REST API Features.....

Retrieve all blog posts in JSON format
Retrieve a single post using slug
Retrieve all categories
Retrieve posts filtered by category
RESTful URL structure
Clean separation between HTML views and API logic

......Tech Stack......

Backend: Python, Django, Django REST Framework
Frontend: HTML, Bootstrap (Django Templates)
Database: SQLite (development)
Version Control: Git & GitHub

......API Endpoints Documentation......


Base URL /api/
All endpoints below are relative to this base path.

#Authentication

...Register User ...
Endpoint POST /auth/register/
Request Body
{
  "username": "sujan",
  "email": "sujan@example.com",
  "password": "strongpassword123"
}
Response (201 Created)

{
  "message": "User registered successfully"
}

....Login User ...
Endpoint POST /auth/login/
Request Body
{
  "username": "sujan",
  "password": "strongpassword123"
}
Response (200 OK)
{
  "message": "Login successful"
}

....Logout User....
Endpoint POST /auth/logout/
Response (200 OK)
{
  "message": "Logout successful"
}


#Categories

...List Categories ...
Endpoint GET /categories/
Response (200 OK)
[
  {
    "id": 1,
    "name": "Technology",
    "slug": "technology"
  }
]


...Get Posts by Category...

Endpoint GET /categories/<slug>/posts/
Response (200 OK)
[
  {
    "id": 5,
    "title": "Django REST Basics",
    "slug": "django-rest-basics"
  }
]


#Posts
...List All Posts...

Endpoint GET /posts/
Response (200 OK)
[
  {
    "id": 1,
    "title": "First Blog",
    "slug": "first-blog",
    "category": "Technology",
    "author": "sujan",
    "created_at": "2026-01-01"
  }
]


...Create Post...

Endpoint POST /posts/create/
Authentication Required 
Request Body
{
  "title": "New Blog",
  "content": "This is my content",
  "category": 1
}
Response (201 Created)
{
  "message": "Post created successfully",
  "slug": "new-blog"
}

....Retrieve Single Post...

Endpoint GET /posts/<slug>/
Response (200 OK)
{
  "title": "New Blog",
  "content": "This is my content",
  "category": "Technology",
  "author": "sujan"
}

...Update Post...

Endpoint PUT /posts/<slug>/update/
Authentication Required  (Owner only)
Request Body
{
  "title": "Updated Title",
  "content": "Updated content"
}
Response (200 OK)
{
  "message": "Post updated successfully"
}

...Delete Post...

Endpoint DELETE /posts/<slug>/delete/
Authentication Required  (Owner only)
Response (204 No Content)

#Comments

....List Comments for a Post...
Endpoint GET /posts/<post_slug>/comments/
Response (200 OK)
[
  {
    "id": 3,
    "user": "ram",
    "content": "Great post!"
  }
]


...Create Comment...

Endpoint POST /posts/<post_slug>/comments/create/
Authentication Required 
Request Body
{
  "content": "Very helpful article"
}
Response (201 Created)
{
  "message": "Comment added successfully"
}


....Update Comment....

Endpoint PUT /comments/<comment_id>/update/
Authentication Required (Owner only)
Request Body
{
  "content": "Updated comment"
}
Response (200 OK)
{
  "message": "Comment updated successfully"
}

.....Delete Comment....

Endpoint DELETE /comments/<comment_id>/delete/
Authentication Required  (Owner only)
Response (204 No Content)

.....Testing......

Unit tests were implemented using Django’s TestCase.
The tests cover:

    Post creation
    Comment creation
    Homepage rendering
All tests pass successfully.

.....Conclusion....

This project demonstrates:
    Django MVC architecture
    REST API design principles
    Relational database usage
    Separation of concerns between web views and APIs
    Practical testing and version control practices