from django import forms
from .models import Activity, Comment


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'content', 'excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
