# forms.py
from django import forms

class jobseekerform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    # Add other fields as needed


