from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit = True):
        user = super(CustomUserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def save(self, commit = True):
        user = super(CustomUserChangeForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user

class UserEditForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
            'experience_in_years',
            'phone'
            ]