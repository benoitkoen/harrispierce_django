from django import forms
from .models import Profile

class SendForm(forms.Form):

    Recipient = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter a friend\'s username'}))
