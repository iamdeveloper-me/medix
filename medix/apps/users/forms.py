from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PricingForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pricing']
      
class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender','phone','image']

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class ProfessionalOverviewForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description','experience']

class UserTypeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['custom_role']

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

class PracticeUserForm(forms.ModelForm):
    
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']

class PracticeSignupForm(forms.ModelForm):
    phone = forms.CharField(required=True)
    class Meta:
        model = Profile
        fields = ['gender','phone']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender', False)
        if self.instance.gender == gender:
            raise ValidationError("required")
        return None

class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['national_identification_number','gender','phone']

class InstitutionSignupForm(forms.ModelForm):
    trading_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    contact_person = forms.CharField(required=True)

    class Meta:
        model = Profile
        fields = ['trading_name','address_of_institution','contact_person','phone']

    # def clean_address_of_institution(self):
    #     address_of_institution = self.cleaned_data.get('address_of_institution', False)
    #     if self.instance.address_of_institution == address_of_institution:
    #         raise ValidationError("required")
    #     return None


class InsuranceProviderSignupForm(forms.ModelForm):
    trading_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    contact_person = forms.CharField(required=True)

    class Meta:
        model = Profile
        fields = ['trading_name','address_of_institution','contact_person','phone']

class EmergencyServiceSignupForm(forms.ModelForm):
    trading_name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    contact_person = forms.CharField(required=True)

    class Meta:
        model = Profile
        fields = ['emergency_services','trading_name','address_of_institution','contact_person','phone']


class EmergencyServiceForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['emergency_services']

    def clean_emergency_services(self):
        emergency_services = self.cleaned_data.get('emergency_services', False)
        if self.instance.emergency_services == emergency_services:
            raise ValidationError("This field is required")
        return None

class PracticeSpecialisationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['practice']
        # exclude = ['custom_role']

    def clean_practice(self):
        practice = self.cleaned_data.get('practice', False)
        if self.instance.practice == practice:
            raise ValidationError("This field is required")
        return None

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['institution']

    def clean_institution(self):
        institution = self.cleaned_data.get('institution', False)
        if self.instance.institution == institution:
            raise ValidationError("This field is required")
        return None