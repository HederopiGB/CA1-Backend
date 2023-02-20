from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    # Retrieve all Post objects and order them by creation date
    posts = Post.objects.all().order_by('-created_on')
    # Construct a dictionary with the posts and render the blog index page with that context
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    # Retrieve all Post objects with the given category and order them by creation date
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    # Construct a dictionary with the posts and category, and render the blog category page with that context
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    # Retrieve the Post object with the given primary key
    post = Post.objects.get(pk=pk)
    # Initialize a CommentForm object to be used to add comments to the post
    form = CommentForm()
    if request.method == 'POST':
        # If a POST request was sent, retrieve the form data and validate it
        form = CommentForm(request.POST)
        if form.is_valid():
            # If the form data is valid, create a new Comment object and save it
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    # Retrieve all comments for the post
    comments = Comment.objects.filter(post=post)
    # Construct a dictionary with the post, comments, and form, and render the blog detail page with that context
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog_detail.html", context)

"""def add_post(request):
    form = AddPost(request.POST or None)
    post = None
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post = Post(
                title = form.cleaned_data["title"],
                body = form.cleaned_data["body"],
                categories = form.cleaned_data["categories"],
            )
            post.save()
    context = {
        "form": form,
        "post": post,
    }
    
    return render(request, "add_post.html", context)"""
        

def homepage(request):
    # Render the homepage
    return render(request, "homepage.html")