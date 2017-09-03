from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from harrispierce.models import Article, Journal, Section


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['user_name', 'password']

    def clean(self, *args, **kwargs):
        user_name = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password')
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            if not user:
                raise forms.ValidationError("Sorry, invalid username or password.")

        return super(LoginForm, self).clean(*args, **kwargs)


class NewUserForm(forms.ModelForm):
    user_name = forms.CharField(max_length=30, label='Username')
    email = forms.EmailField(max_length=254, label='Email')  # help_text='Required. Inform a valid email address.'
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        user_name = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password')
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            if User.objects.filter(username=user_name).exists() or User.objects.filter(email=email).exists():
                raise forms.ValidationError("That user or email is already taken.")

        return super(NewUserForm, self).clean(*args, **kwargs)


class SearchForm(forms.Form):

    Keyword = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Trump, Brexit, Syria...'}))
    Sources = forms.ModelMultipleChoiceField(
        queryset=Journal.objects.all().values_list('name', flat=True),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'section_cb2'})
    )
    Date = forms.CharField(widget=forms.SelectDateWidget)
    Quantity = forms.CharField(widget=forms.NumberInput)

