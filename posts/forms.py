from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('title', 'athlete', 'content', 'excerpt')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'athlete': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.TextInput(attrs={'class': 'form-control'}),
        }
