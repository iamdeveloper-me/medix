from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView,  UpdateView, DeleteView, View, TemplateView
from users.models import Profile, Education
from django.contrib.auth.models import User
from .forms import UserTypeForm, PracticeSignupForm, UserForm, PatientSignupForm, InstitutionSignupForm, InsuranceProviderSignupForm, EmergencyServiceSignupForm, EmergencyServiceForm, PracticeSpecialisationForm, InstitutionForm, PracticeUserForm, ProfessionalOverviewForm, ProfileInfoForm, ProfileUserForm, PricingForm, EducationForm
from django.views import View
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        return redirect('user-type/step1/')
  
class UserFormSubmitView(View):
    def get(self,request):
        messages.success(self.request, 'Successfully registered')
        return render(request,"users/form_submit.html")


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


class PracticeStep2CreateView(CreateView):
    model = Profile
    form_class = PracticeSpecialisationForm
    template_name = 'registration/select_specialisation.html'
    success_url = '/practice/signup/step3/'
    
    def form_valid(self, form, **kwargs):
        spec_type = form.save(commit=False)
        spec_type.custom_role = 1
        spec_type.practice = self.request.POST.get('practice')
        spec_type.save()
        return redirect(self.success_url+str(spec_type.id))

class InstitutionStep2CreateView(CreateView):
    model = Profile
    form_class = InstitutionForm
    template_name = 'registration/select_institution.html'
    success_url = '/institution/signup/step3/'
    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.custom_role = 2
        form.institution = self.request.POST.get('institution')
        form.save()
        return redirect(self.success_url+str(form.id))

        
class EmergencyServiceStep2CreateView(CreateView):
    model = Profile
    form_class = EmergencyServiceForm
    template_name = 'registration/select_emergency_service.html'
    success_url = '/emergency-service/signup/step3/'
    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        form.custom_role = 3
        form.emergency_services = self.request.POST.get('emergency_services')
        form.save()
        return redirect(self.success_url+str(form.id))

    # def get_context_data(self, **kwargs):
    #     context = super(SavedOffLineListView, self).get_context_data(**kwargs)
    #     context['object_list'] = self.model.objects.filter(created_by=self.request.user)
    #     return context

class PracticeSignupStep3View(View):
    def get(self,request,pk):
        form = PracticeSignupForm
        userform = PracticeUserForm
        return render(self.request,'registration/practice.html',
            {'form':form,'userform':userform,'pk':pk})

    def post(self,request,pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        practice_form = PracticeSignupForm(request.POST,instance=profile)
        if user_form.is_valid() and practice_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.username = request.POST.get('email')
                user.is_active = False
                user.save()
                practice_obj = practice_form.save(commit=False)
                practice_obj.user = user
                practice_obj.save()
                # frm = settings.DEFAULT_FROM_EMAIL
                # ctx = {'root_url':settings.ROOT_URL,'email':request.POST.get('email'),'password':request.POST.get('password')}
                # html_content = render_to_string('users/email.html',ctx)
                # email = EmailMessage("Password and email id send on your authorised mail", html_content,frm,to=[user.email])
                # email.content_subtype = "html" 
                # email.send()
            except Exception as e:
                messages.error(self.request, 'Email already exists')
                return HttpResponseRedirect('/practice/signup/step3/'+str(pk))
        else:
            form = PracticeSignupForm
            userform = UserForm
            messages.error(self.request, 'Please select gender')
            return render(self.request,'registration/practice.html',
                {'form':form,'userform':userform,'pk':pk})
        # messages.success(self.request, 'Successfully registered.Please check your authorised email')
        return HttpResponseRedirect('/form/submit/')

class PatientSignupStep2View(View):
    def get(self,request):
        patient_form = PatientSignupForm
        user_form = UserForm
        return render(self.request,'registration/patient.html',{'patient_form':patient_form,'user_form':user_form,})

class InstitutionSignupStep3View(View):
    def get(self, request, pk):
        institution_form = InstitutionSignupForm
        user_form = UserForm
        return render(self.request,'registration/institution.html',{'institution_form':institution_form,'user_form':user_form,'pk':pk})

    def post(self, request, pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        institution_form = InstitutionSignupForm(request.POST, instance=profile)
        if user_form.is_valid() and institution_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.username = request.POST.get('email')
                user.is_active = False
                user.save()
        
                institution_obj = institution_form.save(commit=False)
                institution_obj.user = user
                institution_obj.save()
                # frm = settings.DEFAULT_FROM_EMAIL
                # ctx = {'root_url':settings.ROOT_URL,'email':request.POST.get('email'),'password':request.POST.get('password')}
                # html_content = render_to_string('users/email.html',ctx)
                # email = EmailMessage("Password and email id send on your authorised mail", html_content,frm,to=[user.email])
                # email.content_subtype = "html" 
                # email.send()
            except Exception as e:
                messages.error(self.request, 'Email already exists')
                return HttpResponseRedirect('/institution/signup/step3/'+str(pk))
        else:
            return render(self.request,'registration/institution.html',
                {'user_form':user_form,'institution_form':institution_form})
        # messages.success(self.request, 'Successfully registered.Please check your authorised email')
        # return HttpResponseRedirect('/institution/signup/step3/'+str(pk))
        return HttpResponseRedirect('/form/submit/')

class InsuranceProviderSignupStep2View(View):
    def get(self, request):
        insurance_form = InsuranceProviderSignupForm
        user_form = UserForm
        return render(self.request,'registration/insurance_provider.html',{'insurance_form':insurance_form,'user_form':user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        # profile = Profile.objects.get(pk=pk)
        insurance_form = InsuranceProviderSignupForm(request.POST)
        if user_form.is_valid() and insurance_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.username = request.POST.get('email')
                user.is_active = False
                user.save()
                insurance_obj = insurance_form.save(commit=False)
                insurance_obj.custom_role = 4
                insurance_obj.user = user
                insurance_obj.save()
                # frm = settings.DEFAULT_FROM_EMAIL
                # ctx = {'root_url':settings.ROOT_URL,'email':request.POST.get('email'),'password':request.POST.get('password')}
                # html_content = render_to_string('users/email.html',ctx)
                # email = EmailMessage("Password and email id send on your authorised mail", html_content,frm,to=[user.email])
                # email.content_subtype = "html" 
                # email.send()
            except Exception as e:
                messages.error(self.request, 'Email already exists')
                return HttpResponseRedirect('/insurance/signup/step2/')
        else:
            return render(self.request,'registration/emergency_service.html',
                {'user_form':user_form,'insurance_form':insurance_form})
        # messages.success(self.request, 'Successfully registered.Please check your authorised email')
        # return HttpResponseRedirect('/insurance/signup/step2/')
        return HttpResponseRedirect('/form/submit/')

class EmergencyServiceSignupStep3View(View):
    def get(self,request,pk):
        service_form = EmergencyServiceSignupForm
        user_form = UserForm
        return render(self.request,'registration/emergency_service.html',{'service_form':service_form,'user_form':user_form,'pk':pk})

    def post(self,request,pk):
        user_form = UserForm(request.POST)
        profile = Profile.objects.get(pk=pk)
        service_form = EmergencyServiceSignupForm(request.POST,instance=profile)
        if user_form.is_valid() and service_form.is_valid():
            try:
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.username = request.POST.get('email')
                user.is_active = False
                user.save()
                service_obj = service_form.save(commit=False)
                service_obj.user = user
                service_obj.save()
                # frm = settings.DEFAULT_FROM_EMAIL
                # ctx = {'root_url':settings.ROOT_URL,'email':request.POST.get('email'),'password':request.POST.get('password')}
                # html_content = render_to_string('users/email.html',ctx)
                # email = EmailMessage("Password and email id send on your authorised mail", html_content,frm,to=[user.email])
                # email.content_subtype = "html" 
                # email.send()
            except Exception as e:
                messages.error(self.request, 'Email already exists')
                return HttpResponseRedirect('/emergency-service/signup/step3/'+str(pk))
        else:
            return render(self.request,'registration/emergency_service.html',
                {'user_form':user_form,'service_form':service_form})
        # messages.success(self.request, 'Successfully registered.Please check your authorised email')
        # return HttpResponseRedirect('/emergency-service/signup/step3/'+str(pk))
        return HttpResponseRedirect('/form/submit/')

class LoginView(View):
    def get(self, request):
        # if request.user.is_authenticated:
        return render(request, 'users/login.html')

    def post(self, request):
        # import pdb; pdb.set_trace()
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            role = Profile.objects.filter(user_id=user.id)
            if user.is_superuser and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin/dashboard/')
            elif role[0].custom_role==1 and user.is_active and user.is_staff==False:
                login(request, user)
                return HttpResponseRedirect('/dashboard/practice/'+str(request.user.profile.id))
            elif role[0].custom_role==2 and user.is_active and user.is_staff==False:
                login(request, user)
                return HttpResponseRedirect('/dashboard/institution/')
            elif role[0].custom_role==3 and user.is_active and user.is_staff==False:
                login(request, user)
                return HttpResponseRedirect('/dashboard/emergency-service/')
            elif role[0].custom_role==4 and user.is_active and user.is_staff==False:
                login(request, user)
                return HttpResponseRedirect('/dashboard/health-insurance/')
            else:
                return HttpResponse("Inactive user.")
        else:
            messages.success(self.request, 'You are not authorised to login. Admin approval pending')
            return HttpResponseRedirect('/user-type/step1/')

        return render(request, "users/user_type_form.html")

class AdminDashboardView(View):
    def get(self, request):
        return render(request, 'admin/dashboard.html')

class PracticeDashboardView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            profile_info = ProfileInfoForm
            user_info= ProfileUserForm
            return render(request, 'dashboard/practice.html',{'profile_info':profile_info,'user_info':user_info,'pk':pk})

    def post(self, request, pk):
        user_info = ProfileUserForm(request.POST,instance=User.objects.get(pk=request.user.id))
        profile = Profile.objects.get(pk=pk)
        profile_info = ProfileInfoForm(request.POST,request.FILES,instance=profile)
        if user_info.is_valid() and profile_info.is_valid():
            user = user_info.save(commit=False)
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            profile_obj= profile_info.save(commit=False)
            profile_obj.user = user
            profile_obj.image  = request.FILES.get('image')
            profile_obj.gender = request.POST.get('gender')
            profile_obj.phone = request.POST.get('phone')
            profile_obj.save()
        else:
            messages.error(request, 'Invalid')
            return HttpResponseRedirect('/dashboard/practice/'+str(pk))
        return HttpResponseRedirect('/dashboard/practice/'+str(pk))

class PracticeInfoDetailView(DetailView):
    model = Profile
    template_name = 'practice/profile_detail.html'

class ProfessionalOverviewUpdate(UpdateView): 
    model = Profile
    form_class = ProfessionalOverviewForm 
    template_name = 'dashboard/overview.html'
    success_url = '/create/overview/'
    def form_valid(self, form, **kwargs):
        overview = form.save(commit=False)
        overview.description = self.request.POST.get('description')
        overview.experience = self.request.POST.get('experience')
        overview.save()
        return redirect(self.success_url+str(self.request.user.profile.id))

class ProfessionalOverviewDetail(DetailView):
    model = Profile
    template_name = 'practice/overview_detail.html'

class PriceUpdateView(UpdateView):
    model = Profile
    form_class = PricingForm 
    template_name = 'dashboard/pricing.html'
    success_url = '/price/'
    def form_valid(self, form, **kwargs):
        price = form.save(commit=False)
        price.pricing = self.request.POST.get('price')
        price.save()
        return redirect(self.success_url+str(self.request.user.profile.id))

class PriceDetail(DetailView):
    model = Profile
    template_name = 'dashboard/price_detail.html'

class EducationCreateView(CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'practice/education.html'
    success_url = '/create/education/'
    def form_valid(self, form, **kwargs):
        form = form.save(commit=False)
        user = User.objects.get(pk=self.request.user.id)
        form.user = user
        form.qualification = self.request.POST.get('qualification')
        form.save()
        return redirect(self.success_url)

# class EducationUpdateView(UpdateView):
    # def get(self, request, pk):
    #     if request.user.is_authenticated:
    #         education_form = EducationForm
    #         specialisation_form = PracticeSpecialisationForm
    #         return render(request, 'dashboard/education.html',{'education_form':education_form,'specialisation_form':specialisation_form,'pk':pk})

    # def post(self, request, pk):
    #     education_form = EducationForm(request.POST,instance=User.objects.get(pk=request.user.id))
    #     specialisation_form = PracticeSpecialisationForm(request.POST,instance=profile)
    #     if education_form.is_valid() and specialisation_form.is_valid():
    #         education = education_form.save(commit=False)
    #         education.qualification = request.POST.get('first_name')
            
    #         education.save()
    #         specialisation= specialisation_form.save(commit=False)
    #         specialisation.user = user
    #         specialisation.phone = request.POST.get('phone')
    #         specialisation.save()
    #     else:
    #         messages.error(request, 'Invalid')
    #         return HttpResponseRedirect('/dashboard/practice/'+str(pk))
    #     return HttpResponseRedirect('/dashboard/practice/'+str(pk))



class InstitutionDashboardView(View):
    def get(self, request):
        return render(request, 'dashboard/institution.html')

class EmergencyServicesDashboard(View):
    def get(self, request):
        return render(request, 'dashboard/emergency-services.html')

class HealthInsuranceDashboard(View):
    def get(self, request):
        return render(request, 'dashboard/health_insurance.html')

class LogoutView(View):
    def get(self,request):
        if request.user.username:
            logout(request)
        return HttpResponseRedirect('/user-type/step1/')
