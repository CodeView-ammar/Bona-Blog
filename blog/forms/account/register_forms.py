# # Django imports
# from django import forms
#
#
# class UserRegisterForm(forms.Form):
#     """
#         Creates User registration form for signing up.
#     """
#
#     username = forms.CharField(widget=forms.TextInput(attrs={
#             "name": "username", "class": "input100",
#             "placeholder": "Username"
#         }))
#
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#             "name": "email", "class": "input100",
#             "placeholder": "Email"
#         }))
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#             "name": "password",  "class": "input100",
#             "placeholder": "Password"
#         }))

# Django imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """
        Creates User registration form for signing up.
    """

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

    email = forms.EmailField(widget=
                             forms.EmailInput(attrs={
                                 "name": "email", "class": "input100",
                                 "placeholder": "Email"
                                                    }
                                              ),
                             )
    password1 = forms.CharField(widget=
                                forms.PasswordInput(attrs={
                                 "name": "password1", "class": "input100",
                                 "placeholder": "Password"
                                                    }
                                                    ),
                                )

    password2 = forms.CharField(widget=
                                forms.PasswordInput(attrs={
                                 "name": "password2", "class": "input100",
                                 "placeholder": "Confirm Password"
                                                    }

                                                    ),
                                )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {

            "username": forms.TextInput(attrs={
                "name": "username", "class": "input100",
                "placeholder": "Username"
            }),


        }

