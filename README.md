Django Blog Writing Platform

A clean, structured, and practical blog writing platform built with Django. This project is designed to reflect real-world backend development practices, focusing on clarity, maintainability, and functionality rather than unnecessary complexity.

This repository represents disciplined learning translated into working software.

....Features....

User authentication (login / logout)
Create, edit, and delete blog posts
Category-based post organization and filtering
Comment system for blog posts (users can read and add comments)
Admin panel for managing posts, categories, comments, and users
Secure CSRF-protected forms
Clean and minimal UI using Django templates


....Tech Stack....

Backend: Python, Django
Frontend: HTML, CSS, Bootstrap (Django Templates)
Database: SQLite (development)
Version Control: Git & GitHub


API Documentation 

1 Project Overview
2️ Features
3️ API Endpoints
4️ Authentication
5️ Conclusion



.... Project Overview....
This is a Blog Platform developed using Django.
Users can create posts, view posts by category, and add comments.
The project follows MVC architecture and includes unit testing.

....Features....
- User authentication (login & logout)
- Create, view, edit, delete blog posts
- Category-based post filtering 
- Searching Post by title or content
- Comment system
- Unit testing using Django TestCase

.......API Endpoints Documentation .......

......Get All Posts.....
URL: /
Method: GET
Description: Displays a list of all published blog posts on the homepage.
Response: HTTP 200 OK

.......Create New Post .......

URL: /post/create/
Method: POST
Authentication: Required
Data Parameters:
    title: string
    content: text
    category: integer
Description: Allows logged-in users to create a new blog post.


......View Single Post (view More)........

URL: /post/<id>/
Method: GET
Description: Displays detailed view of a single post along with comments.


.......Add Comment........

URL: /post/<id>/comment/
Method: POST
Authentication: Required
Data Parameters:
    content: text
Description: Allows users to add comments to a specific post.


....... Testing .......

Unit tests were implemented using Django's TestCase.
The tests cover post creation, comment creation, and homepage view.
All tests pass successfully.

......Conclusion ......

This project demonstrates basic CRUD operations, relational database usage,
and Django testing practices. 