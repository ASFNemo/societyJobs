from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from models import MyUser, studentData


class LoginForm(forms.Form):
    email = forms.CharField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrationForm(forms.Form):

    email = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    # user_type_field = forms.ChoiceField(choices=user_Types)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        #todo: find a good password validation method to call here

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            raise forms.ValidationError("email already in use")
        except MyUser.DoesNotExist:
            return email
        except:
             raise forms.ValidationError("there was an error, please try again soon")


# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = MyUser
#         fields = ('email', 'password')
#
#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(UserCreationForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class StudentDetailsForm(forms.Form):

    first_name = forms.CharField()
    surname = forms.CharField()
    course = forms.CharField()
    university = forms.CharField()
    countryOfStudy = forms.CharField()


class companyDetailsForm(forms.Form):
    company_name = forms.CharField()
    company_website = forms.CharField()
    HQ_city = forms.CharField()
    industry = forms.CharField()


class SocietyDetailsForm(forms.Form):
    society_name = forms.CharField()
    society_university = forms.CharField()
    society_website = forms.CharField()
    society_FB = forms.CharField()

