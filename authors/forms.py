from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'fullName',
            'bio',
            'image',
        ]
        widgets = {
        'fullName': forms.TextInput(attrs={'class': 'form-control'}),
        'bio': forms.Textarea(attrs={'class': 'form-control'}),
        'image': forms.FileInput(attrs={'class': 'custom-file'}),
    }
