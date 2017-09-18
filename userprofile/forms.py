from django import forms
from .models import Profile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('choices', 'friends', 'following')