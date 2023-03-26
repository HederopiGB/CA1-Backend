from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm, AddPostForm
from django.http import HttpResponseForbidden
from django.urls import reverse


def blog_index(request):
    # Anti-CSS attack security check
    if request.method == 'POST' and request.POST.get('name') and '<style>' in request.POST['name']:
        return HttpResponseForbidden()

    # Anti-SQL injection security check
    name = request.GET.get('name', '')
    if ';' in name:
        return HttpResponseForbidden()

    # Redirection security check
    if request.is_secure():
        return HttpResponseForbidden()
    
    
    # Retrieve all Post objects and order them by creation date
    posts = Post.objects.all().order_by('-created_on')
    # Construct a dictionary with the posts and render the blog index page with that context
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_category(request, category):
    # Anti-CSS attack security check
    if request.method == 'POST' and request.POST.get('name') and '<style>' in request.POST['name']:
        return HttpResponseForbidden()

    # Anti-SQL injection security check
    name = request.GET.get('name', '')
    if ';' in name:
        return HttpResponseForbidden()

    # Redirection security check
    if request.is_secure():
        return HttpResponseForbidden()
    
    
    # Retrieve all Post objects with the given category and order them by creation date
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    # Construct a dictionary with the posts and category, and render the blog category page with that context
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


def blog_detail(request, pk):
    # Anti-CSS attack security check
    if request.method == 'POST' and request.POST.get('name') and '<style>' in request.POST['name']:
        return HttpResponseForbidden()

    # Anti-SQL injection security check
    name = request.GET.get('name', '')
    if ';' in name:
        return HttpResponseForbidden()

    # Redirection security check
    if request.is_secure():
        return HttpResponseForbidden()
    
    
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

def add_post(request):
    form = AddPostForm(request.POST or None)
    post = None
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = form.save()
    context = {
        "form": form,
        "post": post,
    }
    return render(request, "add_post.html", context)
        

def homepage(request):
    # Anti-CSS attack security check
    if request.method == 'POST' and request.POST.get('name') and '<style>' in request.POST['name']:
        return HttpResponseForbidden()

    # Anti-SQL injection security check
    name = request.GET.get('name', '')
    if ';' in name:
        return HttpResponseForbidden()

    # Redirection security check
    if request.is_secure():
        return HttpResponseForbidden()
    
    
    # Render the homepage
    return render(request, "homepage.html")