from django import forms
from django.shortcuts import render


class SmulForm(forms.Form):
    url = forms.URLField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Input your URL'}))
    #,widget=forms.TextInput(attrs={'placeholder': 'Input your URL'})