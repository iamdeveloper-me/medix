from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    
    path('user-type/step1/',views.UserTypeStep1View.as_view(), name='user-type-list'),
    path('practice/signup/step2/',views.PracticeSignupStep2View.as_view(), name='practice-signup'),
    path('patient/signup/step2/',views.PatientSignupStep2View.as_view(), name='patient-signup'),
    path('institution/signup/step2/',views.InstitutionSignupStep2View.as_view(), name='institution-signup'),
    # path('service/registration/',views.EmergencyServiceRegistration.as_view(), name='emergency-service-registration'),

    path('insurance/signup/step2/',views.InsuranceProviderSignupStep2View.as_view(), name='insurance-provider-signup'),

]