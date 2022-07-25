from cProfile import label
from dataclasses import fields
from socket import fromshare
from tkinter.ttk import Widget
from unittest.util import _MAX_LENGTH
from django import forms
from .models import Buyer
import re

class Buyerform(forms.ModelForm):
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput())
    name = forms.CharField(label = 'Name', widget = forms.TextInput())
    phone = forms.CharField(label = 'Phone', widget = forms.NumberInput())
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    cn_password = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput())

    class Meta:
        model = Buyer
        fields = ('email', 'name', 'phone', 'password')

    def clean_name(self):
        dname = self.cleaned_data['name']
        if not re.match('^[A-Za-z]+$',dname):
            raise forms.ValidationError('Name cannot contain numbers')
        return dname
    
    def clean_cn_password(self):
        pswd = self.cleaned_data['password']
        cnpswd = self.cleaned_data['cn_password']
        if pswd == cnpswd:
            return cnpswd
        else:
            raise forms.ValidationError("Password doesn't match")
