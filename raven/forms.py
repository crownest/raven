# Django
from django import forms
from django.contrib.auth import authenticate, get_user_model, login

# Local Django
from users.models import User


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user = authenticate(email=email, password=password)
            if not self.user:
                raise forms.ValidationError("This user does not exist")
        return super(LoginForm, self).clean(*args, **kwargs)
    def get_user(self):
        return self.user
