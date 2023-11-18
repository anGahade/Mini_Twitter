from posts.models import Post
from django.forms import ModelForm
from django import forms


class PostForm(ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }