from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView,View
from users.models import Profile
from django.contrib.auth.models import User
from .forms import UserTypeForm, PracticeSignupForm, UserForm, PatientSignupForm, InstitutionSignupForm, InsuranceProviderSignupForm
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse


class UserTypeStep1View(CreateView):
    model = Profile
    form_class = UserTypeForm
    template_name = 'users/user_type_form.html'
    
    def form_valid(self, form, **kwargs):
        user_type = form.save(commit=False)
        if user_type.custom_role==0:
           return redirect('/patient/signup/step2/')
        elif user_type.custom_role==1:
            return redirect('/practice/signup/step2/')
        elif user_type.custom_role==2:
            return redirect('/institution/signup/step2/')
        elif user_type.custom_role==3:
            return render(self.request,'registration/emergency_service.html')
        elif user_type.custom_role==4:
            return redirect('/insurance/signup/step2/')


class PracticeSignupStep2View(View):
    def get(self,request):
        form = PracticeSignupForm
        userform = UserForm
        return render(self.request,'registration/practice.html',
            {'form':form,'userform':userform,})

    def post(self,request):
        user_form = UserForm(request.POST)
        practice_form = PracticeSignupForm(request.POST)
        if user_form.is_valid() and practice_form.is_valid():
            user = user_form.save(commit=False)
            user.username = request.POST.get('email')
            user.save()
            practice_obj = practice_form.save(commit=False)
            practice_obj.user = user
            practice_obj.save()
        else:
            return render(self.request,'registration/practice.html',
                {'form':user_form,'userform':practice_form,})

        return HttpResponseRedirect('/practice/signup/step2/')

class PatientSignupStep2View(View):
    def get(self,request):
        patient_form = PatientSignupForm
        user_form = UserForm
        return render(self.request,'registration/patient.html',{'patient_form':patient_form,'user_form':user_form,})


class InstitutionSignupStep2View(View):
    def get(self,request):
        institution_form = InstitutionSignupForm
        user_form = UserForm
        return render(self.request,'registration/institution.html',{'institution_form':institution_form,'user_form':user_form,})

    def post(self,request):
        user_form = UserForm(request.POST)
        institution_form = InstitutionSignupForm(request.POST)
        if user_form.is_valid() and institution_form.is_valid():
            user = user_form.save(commit=False)
            user.username = request.POST.get('email')
            user.save()
            institution_obj = institution_form.save(commit=False)
            institution_obj.user = user
            institution_obj.save()
        else:
            return render(self.request,'registration/institution.html',
                {'user_form':user_form,'institution_form':institution_form})
        return HttpResponseRedirect('/practice/signup/step2/')

class InsuranceProviderSignupStep2View(View):
    def get(self,request):
        insurance_form = InsuranceProviderSignupForm
        user_form = UserForm
        return render(self.request,'registration/insurance_provider.html',{'insurance_form':insurance_form,'user_form':user_form,})

    def post(self,request):
        user_form = UserForm(request.POST)
        insurance_form = InsuranceProviderSignupForm(request.POST)
        if user_form.is_valid() and insurance_form.is_valid():
            user = user_form.save(commit=False)
            user.username = request.POST.get('email')
            user.save()
            insurance_obj = insurance_form.save(commit=False)
            insurance_obj.user = user
            insurance_obj.save()
        else:
            return render(self.request,'registration/insurance_provider.html',
                {'user_form':user_form,'insurance_form':insurance_form})
        return HttpResponseRedirect('/practice/signup/step2/')


# class InsuranceProviderSignupStep2View(View):
#     def get(self,request):
#         insurance_form = InsuranceProviderSignupForm
#         user_form = UserForm
#         return render(self.request,'registration/insurance_provider.html',{'insurance_form':insurance_form,'user_form':user_form,})








