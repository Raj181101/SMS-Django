from django import forms
from Birthday.models import Birth

class UserRegisterForm(forms.ModelForm): 
    class Meta:
        model=Birth
        fields='__all__'