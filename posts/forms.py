""" Modules """
from django import forms
from .models import Activity, Comment


class ActivityForm(forms.ModelForm):
    """ Creates Activity Form """
    class Meta:
        """ Model, Fields, and Widgets for ActivityForm """
        model = Activity
        fields = ('title', 'content', 'excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """ Creates Comment Form """
    class Meta:
        """ Model, Fields, and Widgets for CommentForm """
        model = Comment
        fields = ('content',)

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
