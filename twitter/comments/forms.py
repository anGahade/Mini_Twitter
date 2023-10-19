from comments.models import Comment
from django.forms import ModelForm
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']
        widgets = {
            'post': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }