# Django
from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': ' Enter Email'}), required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True
    )

    class Meta:
        fields = ('email', 'password')

    def clean(self):
        clean = super(LoginForm, self).clean()

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if not email or not password:
            raise forms.ValidationError('Incorrect email address or password!')

        user = authenticate(email=email, password=password)

        if not user:
            raise forms.ValidationError('Incorrect email address or password!')
        elif not user.is_active:
            raise forms.ValidationError('Your account is not active!')
        else:
            self.user = user

        return self.cleaned_data
