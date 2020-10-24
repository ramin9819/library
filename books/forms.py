from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'image',
            'genre',
            'summary',
        ]

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'genre': forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
        'image': forms.FileInput(attrs={'class': 'custom-file'}),
        'summary': forms.Textarea(attrs={'class': 'form-control'}),
        #'image': forms.FileInput(attrs={'class': 'form-control'}),
    }
        # use bootstrap forms!  ####CHECK#### class="custom-select mr-sm-2"