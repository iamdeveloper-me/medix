from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,View
from users.models import Profile
from django.contrib.auth.models import User
from .forms import UserTypeForm, PracticeSignupForm, UserForm, PatientSignupForm, InstitutionSignupForm, InsuranceProviderSignupForm, EmergencyServiceSignupForm, EmergencyServiceForm, PracticeSpecialisationForm, InstitutionForm
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse


class UserTypeStep1View(CreateView):
    model = Profile
    form_class = UserTypeForm
    template_name = 'users/user_type_form.html'
    
    def form_valid(self, form, **kwargs):
        profile = form.save(commit=False)
        profile.save()
        if profile.custom_role==0:
           return redirect('/patient/signup/step2/')
        elif profile.custom_role==1:
            return redirect('/specialisation/step2/'+str(profile.id))
        elif profile.custom_role==2:
            return redirect('/institution/step2/'+str(profile.id))
        elif profile.custom_role==3:
            return redirect('/emergency-services/step2/'+str(profile.id))
        else:
            return redirect('/insurance/signup/step2/'+str(profile.id))

class SpecialisationStep2UpdateView(UpdateView):
    model = Profile
    form_class = PracticeSpecialisationForm
    template_name = 'registration/select_specialisation.html'
    success_url = '/practice/signup/step3/'
    
    def form_valid(self, form, **kwargs):
        spec_type = form.save(commit=False)
        spec_type.save()
        return redirect(self.success_url+str(spec_type.id))

class InstitutionStep2UpdateView(UpdateView):
    model = Profile
    form_class = InstitutionForm
    template_name = 'registration/select_institution.html'
    success_url = '/institution/signup/step3/'
    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.save()
        return redirect(self.success_url+str(form.id))
        
class EmergencyServiceStep2UpdateView(UpdateView):
    model = Profile
    form_class = EmergencyServiceForm
    template_name = 'registration/select_emergency_service.html'
    success_url = '/emergency-service/signup/step3/'
    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.save()
        return redirect(self.success_url+str(form.id))

class PracticeSignupStep3View(View):
    def get(self,request,pk):
        form = PracticeSignupForm
        userform = UserForm
        return render(self.request,'registration/practice.html',
            {'form':form,'userform':userform,})

    def post(self,request,pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        practice_form = PracticeSignupForm(request.POST,instance=profile)
        if user_form.is_valid() and practice_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = request.POST.get('email')
            user.save()
            practice_obj = practice_form.save(commit=False)
            practice_obj.user = user
            practice_obj.save()
        else:
            return render(self.request,'registration/practice.html',
                {'form':user_form,'userform':practice_form,})

        return HttpResponseRedirect('/practice/signup/step3/'+str(pk))

class PatientSignupStep2View(View):
    def get(self,request):
        patient_form = PatientSignupForm
        user_form = UserForm
        return render(self.request,'registration/patient.html',{'patient_form':patient_form,'user_form':user_form,})

class InstitutionSignupStep3View(View):
    def get(self, request, pk):
        institution_form = InstitutionSignupForm
        user_form = UserForm
        return render(self.request,'registration/institution.html',{'institution_form':institution_form,'user_form':user_form,})

    def post(self, request, pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        institution_form = InstitutionSignupForm(request.POST, instance=profile)
        if user_form.is_valid() and institution_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = request.POST.get('email')
            user.save()
            institution_obj = institution_form.save(commit=False)
            institution_obj.user = user
            institution_obj.save()
        else:
            return render(self.request,'registration/institution.html',
                {'user_form':user_form,'institution_form':institution_form})
        return HttpResponseRedirect('/institution/signup/step3/'+str(pk))

class InsuranceProviderSignupStep2View(View):
    def get(self, request, pk):
        insurance_form = InsuranceProviderSignupForm
        user_form = UserForm
        return render(self.request,'registration/insurance_provider.html',{'insurance_form':insurance_form,'user_form':user_form,})

    def post(self, request, pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        insurance_form = InsuranceProviderSignupForm(request.POST, instance=profile)
        if user_form.is_valid() and insurance_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = request.POST.get('email')
            user.save()
            insurance_obj = insurance_form.save(commit=False)
            insurance_obj.user = user
            insurance_obj.save()
        else:
            return render(self.request,'registration/emergency_service.html',
                {'user_form':user_form,'insurance_form':insurance_form})
        return HttpResponseRedirect('/insurance/signup/step2/'+str(pk))


class EmergencyServiceSignupStep3View(View):
    def get(self,request,pk):
        service_form = EmergencyServiceSignupForm
        user_form = UserForm
        return render(self.request,'registration/emergency_service.html',{'service_form':service_form,'user_form':user_form,})


    def post(self,request,pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        service_form = EmergencyServiceSignupForm(request.POST,instance=profile)
        if user_form.is_valid() and service_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.username = request.POST.get('email')
            user.save()
            service_obj = service_form.save(commit=False)
            service_obj.user = user
            service_obj.save()
        else:
            return render(self.request,'registration/emergency_service.html',
                {'user_form':user_form,'service_form':service_form})
        return HttpResponseRedirect('/emergency-service/signup/step3/'+str(pk))




