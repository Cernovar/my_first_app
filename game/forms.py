from django import forms
from .models import Username

class UsernameForm(forms.ModelForm):
    """Form definition for Username."""
    

    class Meta:
        """Meta definition for Usernameform."""

        model = Username
        fields = ('username',)
        labels = {
            'username': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your name here'}),
        }
 
class CommentsForm(forms.ModelForm):

    class Meta:

        model = Username
        fields = ('username','comments',)
        labels = {
            'comments': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your name here'}),
            'comments': forms.TextInput(attrs={'placeholder': 'Enter your comment here'}), 
            'comments': forms.Textarea(attrs={'rows': 15, 'cols': 122}),
        }