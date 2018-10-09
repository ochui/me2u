from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm
from django_countries.fields import CountryField
from .models import CustomUser

#These User creation form will be use by staff users
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

#These User creation form will be use by staff users
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class CustomSignupForm(SignupForm):

    country = CountryField().formfield()
    def signup(self, request, user):
        user.country = self.cleaned_data['country']
        user.save()
        return user