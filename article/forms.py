from django import forms
from .models import PostComment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['text']

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'summary', 'category']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')