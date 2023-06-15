from . models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numele articolui'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anuntul articolui'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Data Publicarii : 2020-01-01 00:00:00'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Continutul articolui'
            }),
        }
