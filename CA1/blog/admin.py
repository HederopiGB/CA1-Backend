from django.contrib import admin
from blog.models import Post, Category, Comment

# Define admin classes for each model
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

# Register each model and its corresponding admin class with the admin site to each class 
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)