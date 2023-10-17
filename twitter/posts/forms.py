from posts.models import Post
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['user', 'title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }