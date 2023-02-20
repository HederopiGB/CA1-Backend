from django import forms
from django.utils import timezone

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
    

"""class AddPost(forms.Form):
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
            "placeholder": "Body"
        })
    )
    categories = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Categories"
        })
    )
    created_on = forms.DateTimeField(
        widget=forms.HiddenInput(),
        initial=timezone.now()
    )
    last_modified = forms.DateTimeField(
        widget=forms.HiddenInput(),
        initial=timezone.now()
    )"""