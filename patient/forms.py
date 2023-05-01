from django import forms
from .models import *
from django.contrib.auth.models import User


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','gender','age','father_name','mother_name','height','weight','blood_pressure']


class DetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','age','height','weight','blood_pressure']


class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['person','reports']


class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']