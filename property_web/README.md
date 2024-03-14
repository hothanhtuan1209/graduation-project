# PROJECT PROPERTY WEBSITE
This is a project to build a property website, including User, Post, Category, Image, Favorates, Review.
- User: this is User model, each user can have many posts
- Category: this is a model for managing category, each category include many post
- Post: this is a model for managing post.
- Image: this is Image model and each post can have many image
- Favorite: this is a model for managing Favorite post of user.
- Review: this is a model for managing Review, each post can have many Review

## Required
- To run the project, you need to install python version 3.11 or higher and install the environments to use python.
- Install virtual environment

## Documents
- Diagrams:
> https://app.diagrams.net/#G1M_p-oaLSCYTS6CwaTB43IGT8fQAtvyYy#%7B%22pageId%22%3A%222HYW_9K1xufZjpmMfSIS%22%7D

- Analytics documentation
https://docs.google.com/document/d/1sIQv1cb0KxRe1qGgVPHCIVYlIncr9fXF/edit

## How to use
### For Linux or MacOS operating systems, replace py with python
1. First, clone this repository on your computer
> git clone https://github.com/hothanhtuan1209/graduation-project.git

2. Next, move into the directory containing this file:
> cd graduation-project
> cd property_web


3. Checkout to branch develop
> git checkout develop

4. You should create virtual environment and install pyenv
- Create virtual environment named 'venv'
> python -m venv venv

- Run virtual environment for Windows
> .\venv\Scripts\activate

- Run virtual environment for MacOS
> source venv/bin/

- Deactivate a virtual environment
> deactivate

- To install all packages and extensions in project
> pip install -r requirements.txt 

5. Create database
> py manage.py makemigrations property_web
> py manage.py migrate

6. Create superuser
> py manage.py createsuperuser

7. Running server
>py manage.py runserver


## Contribute
 - If you want to contribute to this project, please create a pull request and clearly describe the changes you propose
