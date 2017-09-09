# Django
from django import forms
from django.contrib.auth import authenticate

# Local Django
from colleges.models import College
from departments.models import Department, RegistrationRequest


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}), required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True
    )

    class Meta:
        fields = ('email', 'password')

    def clean(self):
        clean = super(LoginForm, self).clean()

        email = self.cleaned_data.get('email', None)
        password = self.cleaned_data.get('password', None)

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


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}), required=True
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}), required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), required=True
    )
    # college = forms.ModelChoiceField(
    #     queryset=College.objects.all(), empty_label='College', required=True
    # )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(), empty_label='Department', required=True
    )

    class Meta:
        fields = ('email', 'first_name', 'last_name', 'department')

    def clean(self):
        clean = super(RegisterForm, self).clean()

        email = self.cleaned_data.get('email', None)
        department = self.cleaned_data.get('department', None)

        registration_requests = RegistrationRequest.objects.filter(
            email=email, department=department
        )

        if registration_requests:
            raise forms.ValidationError('Registration request already exists!')

        return self.cleaned_data

    def save(self, commit=True):
        registration_request = None

        if commit:
            try:
                registration_request = RegistrationRequest(
                    email=self.cleaned_data.get('email', None),
                    first_name=self.cleaned_data.get('first_name', None),
                    last_name=self.cleaned_data.get('last_name', None),
                    department=self.cleaned_data.get('department', None)
                )
                registration_request.save()
            except:
                registration_request = None

        return registration_request
