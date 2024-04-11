from django import forms
from .models import Content, Comment

class ContentForm(forms.Form):
    class Meta:
        model = Content
        field = ['title','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)