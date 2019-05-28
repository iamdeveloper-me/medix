from .models import Profile
from django import forms
from django.contrib.auth.models import User


class UserTypeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['custom_role']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']


class PracticeSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['practice','gender','phone']

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['national_identification_number','gender','phone']

class InstitutionSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['institution','trading_name','address_of_institution','contact_person','phone']

class InsuranceProviderSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['trading_name','address_of_institution','contact_person','phone']