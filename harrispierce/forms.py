from django import forms


class LoginForm(forms.Form):

    Email = forms.CharField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)

    def login(self):
        return
        # send email using the self.cleaned_data dictionary pass


class NewUserForm(forms.Form):

    Email = forms.CharField(widget=forms.EmailInput)
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(widget=forms.PasswordInput)

    def signup(self):
        return
        # send email using the self.cleaned_data dictionary pass


class SearchForm(forms.Form):

    Keyword = forms.CharField(widget=forms.TextInput)
    Sources = forms.CharField(widget=forms.Textarea)
    Date = forms.CharField(widget=forms.SelectDateWidget)
    Quantity = forms.CharField(widget=forms.NumberInput)
