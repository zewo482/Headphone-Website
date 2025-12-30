from django import forms
from .models import User, Mhp

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class MhpForm(forms.ModelForm):
    class Meta:
        model = Mhp
        fields = '__all__'
