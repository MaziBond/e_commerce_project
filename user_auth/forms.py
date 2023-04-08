from django import forms
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from .models import User, UserProfile


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileUpdateForm(forms.ModelForm):
    country = CountryField().formfield()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'address', 'city', 'country', 'image')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


#  {{ user_form|crispy }}
#             <!-- User form -->
#             {{ profile_form|crispy }}
#             <!-- Profile form -->