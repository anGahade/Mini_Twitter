from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ваш коментар...'}),
        }

    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('post_id', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if post_id:
            self.fields['post_id'] = forms.IntegerField(widget=forms.HiddenInput(), initial=post_id)