from django import forms 

from users.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
        
    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password")
        model = User