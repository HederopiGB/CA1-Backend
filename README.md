# CA1-Backend

This is a simple blog web application built with Django

Description :

The app consists of three main models: Post, Category, and Comment. Post represents individual blog posts and has fields for title, body, created_on, last_modified, and a ManyToManyField relationship with Category. Category represents categories or tags that posts can be associated with, and has a single field for name. Comment represents comments made on individual posts, and has fields for author, body, created_on, and a ForeignKey relationship with Post.
In addition to these models, there are several views defined in views.py that allow for browsing and interacting with the blog. The blog_index view displays a list of all blog posts, ordered by the created_on field. The blog_category view displays a list of blog posts associated with a particular category or tag, also ordered by created_on. The blog_detail view displays the details of a single post, including its comments and a form for adding new comments. Finally, there is a homepage view that simply displays a landing page.
To provide administrative functionality, there are three model admins defined in admin.py for Post, Category, and Comment. These simply inherit from the base ModelAdmin class, and are registered with the Django admin site to allow for management of these models.
Overall, this app provides a simple, functional platform for creating and managing a blog. Its use of Django's built-in admin interface makes it easy to manage posts and comments, while the custom views and templates allow for a clean, user-friendly front-end.


Features :

The following are the key features of the application:

Users can view a list of all blog posts, sorted by date of creation.
Users can view individual blog posts, including the post's title, content, and comments.
Users can leave comments on blog posts, with their name and comment content.

Installation :

To install the application, follow these steps:
Clone the repo git.
Install Django
In a terminal: 
	- Go in the folder 
	- Type “python manage.py makemigrations”
	- Type “python manage.py migrate”
	-Type “python manage.py runserver”
You will land on the homepage of the website then you can use the application and read the posts.

Usage :

To use the application, follow these steps:

View all blog posts on the home page.
Click on an individual blog post to view its details.
Leave a comment on a blog post by filling out the comment form at the bottom of the post detail page.
