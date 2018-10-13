#  * This file is part of me2u project.
#  * (c) Ochui Princewill Patrick <ochui.princewill@gmail.com>
#  * For the full copyright and license information, please view the "LICENSE.md"
#  * file that was distributed with this source code.
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django_countries import countries
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import CustomUser

# These User creation form will be use by staff users


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields

# These User creation form will be use by staff users


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class CustomSignupForm(SignupForm):

    country = CountryField().formfield()

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(
            attrs={
               'class': 'input-bordered',
                'placeholder': _('E-mail address'),
                'autofocus': 'autofocus' 
            }
        )

        self.fields['country'].widget = CountrySelectWidget(
            attrs={
               'class': 'input-bordered',
            },
            choices = [('', _('Select country'))] + list(countries),
            
        )

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
               'class': 'input-bordered',
               'placeholder': _('Password')
            }
        )

        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
               'class': 'input-bordered',
               'placeholder': _('Password (again)')
            }
        )

    def save(self, request):
        # call the parent classes save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.country = self.cleaned_data['country']
        user.save()
        return user


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(
            attrs={
                'class': 'input-bordered',
                'placeholder': _('Username or e-mail'),
                'autofocus': 'autofocus'
            }
        )

        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class': 'input-bordered',
                'placeholder': _('Password'),
            }
        )

class CustomResetPasswordForm(ResetPasswordForm):
    
    def __init__(self, *args, **kwargs):
       super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
       self.fields['email'].widget = forms.EmailInput(
           attrs={
               'class': 'input-bordered',
               'placeholder': _('E-mail address')
           }
       )

class AccountEditForm(forms.ModelForm):
     class Meta:
         model = CustomUser
         fields = ('first_name', 'last_name', 'phone_number', 'date_of_birth', 'country')
         widgets = {
             'first_name':forms.TextInput(
                 attrs={
                     'class': 'input-bordered',
                 }
             ),
             'last_name':forms.TextInput(
                 attrs={
                     'class': 'input-bordered',
                 }
             ),
             'phone_number':forms.TextInput(
                 attrs={
                     'class': 'input-bordered'
                 }
             ),
             'date_of_birth':forms.DateInput(
                 attrs={
                     'class': 'input-bordered'
                 }
             )
         }