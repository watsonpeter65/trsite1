# forms.py
from django import forms

class courseseekerform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    # Add other fields as needed


class jobseekerform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    cv_file = forms.FileField(label='Upload CV', required=False)
    # Add other fields as needed


