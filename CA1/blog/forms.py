from django import forms
from django.utils import timezone
from .models import Post, Category, Comment

# Creating a form for adding comments to a blog post
class CommentForm(forms.Form):
    
    # A field for the author's name with a maximum length of 60 characters
    author = forms.CharField(
        max_length=60,
        
        # Adding CSS classes and a placeholder to the input field
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    
    # A field for the body of the comment, displayed as a textarea
    body = forms.CharField(
        widget=forms.Textarea(
            
            # Adding CSS classes and a placeholder to the textarea
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment !"
            })
    )
    


class AddPostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Content"
        })
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            "class": "form-check-input"
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']