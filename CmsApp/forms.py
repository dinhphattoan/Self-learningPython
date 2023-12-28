

from django import forms
from CmsApp import models


class DocumentaryForm(models.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={
        'label' : 'Username',
        'class': "form-control",
        'id' : "usernametextinput",
        'type' : 'text',
        'placeholder' : "Enter username"
        }))
    password1 = forms.CharField(widget = forms.TextInput(attrs={
        'class': "form-control",
        'id' : "floatingpasswordinput1",
        'type' : 'password',
        'placeholder' : "Enter your password"
        }))
    password2 = forms.CharField(widget = forms.TextInput(attrs={
        'label' : "Confirm Password ",
        'class': "form-control",
        'id' : "floatingpasswordinput2",
        'type' : 'password',
        'placeholder' : "Confirm your password"
        }))
    class Meta:
        fields = ('username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(DocumentaryForm, self).__init__(*args, **kwargs)