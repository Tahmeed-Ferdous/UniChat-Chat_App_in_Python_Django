from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 
                'style': 'height: 80px; font-size: 0.875rem;',
                'rows': '1', 
            }
        ),
        required=True,
    )

    class Meta:
        model = Comment
        fields = ('body',)
#for the template