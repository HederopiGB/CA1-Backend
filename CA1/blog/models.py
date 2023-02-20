from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)  # A category with a name

class Post(models.Model):
    title = models.CharField(max_length=255)  # The title of the post
    body = models.TextField()  # The content of the post
    created_on = models.DateTimeField(auto_now_add=True)  # The date and time the post was created
    last_modified = models.DateTimeField(auto_now=True)  # The date and time the post was last modified
    categories = models.ManyToManyField('Category', related_name='posts')  # The categories associated with the post

class Comment(models.Model):
    author = models.CharField(max_length=60)  # The author of the comment
    body = models.TextField()  # The content of the comment
    created_on = models.DateTimeField(auto_now_add=True)  # The date and time the comment was created
    post = models.ForeignKey('Post', on_delete=models.CASCADE)  # The post that the comment belongs to