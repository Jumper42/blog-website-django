from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "date"]
        labels = {
            "user_name": "Name",
            "email": "Email",
            "text": "Comment"
        }
