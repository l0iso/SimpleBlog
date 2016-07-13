# coding: utf-8
from django import forms
from .models import Comments, BlogPost

class CommentsForm (forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_author','comment_text',)

class PostForm (forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('post_head','post_author','post_text',)
        widgets = {"post_text": forms.widgets.Textarea(attrs={'rows': 2})}
