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

Get All Posts

URL: /api/posts/
Method: GET
Description: Returns a list of all blog posts in JSON format
Response: 200 OK

Get Single Post

URL: /api/posts/<slug>/
Method: GET
Description: Returns detailed information of a single post
Response: 200 OK

Get All Categories

URL: /api/categories/
Method: GET
Description: Returns a list of all blog categories
Response: 200 OK

Get Posts by Category
URL: /api/category/<slug>/posts/
Method: GET
Description: Returns all posts belonging to a specific category
Response: 200 OK

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