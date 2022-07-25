from socket import fromshare
from django import forms
from .models import Registration
import re

class Registrationform(forms.ModelForm):
    name = forms.CharField(label = 'name', widget = forms.TextInput())
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    
    class Meta:
        model = Registration
        fields = ('name', 'password')
    
    def clean_name(self):
        dname = self.cleaned_data['name']
        if not re.match('^[A-Za-z]+$',dname):
            raise forms.ValidationError('Name cannot contain numbers')
        return dname