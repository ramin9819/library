from django import forms
from .models import Profile



# use bootstrap forms!  ####CHECK####

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'prof'
        ]
