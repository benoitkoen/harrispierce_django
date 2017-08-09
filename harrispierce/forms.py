from django import forms
from django.contrib.auth.models import User

from harrispierce.scrapping.scrap_urls import journals


DISPLAY_CHOICES = (
    ("locationbox", "Display Location"),
    ("displaybox", "Display Direction")
)


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['user_name', 'password']

    def login(self):
        return
        # send email using the self.cleaned_data dictionary pass


class NewUserForm(forms.ModelForm):
    user_name = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=254, label='Email')  # help_text='Required. Inform a valid email address.'
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']

    def clean_email(self):
        return
        # send email using the self.cleaned_data dictionary pass


class SearchForm(forms.Form):

    Keyword = forms.CharField(widget=forms.TextInput)
    Sources = forms.CharField(widget=forms.Textarea)
    Date = forms.CharField(widget=forms.SelectDateWidget)
    Quantity = forms.CharField(widget=forms.NumberInput)
