from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'summary', 'director', 'genre', 'rating')
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 0,
                'max': 5,
                'step': 0.5,
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('content', )
