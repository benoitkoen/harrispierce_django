from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    #Email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    def login(self):
        return
        # send email using the self.cleaned_data dictionary pass


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

    #Email = forms.CharField(widget=forms.EmailInput)
    #Password = forms.CharField(widget=forms.PasswordInput)
    #Confirm_Password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        return
        # send email using the self.cleaned_data dictionary pass


class SearchForm(forms.Form):

    Keyword = forms.CharField(widget=forms.TextInput)
    Sources = forms.CharField(widget=forms.Textarea)
    Date = forms.CharField(widget=forms.SelectDateWidget)
    Quantity = forms.CharField(widget=forms.NumberInput)
