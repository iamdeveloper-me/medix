from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    
    path('user-type/step1/',views.UserTypeStep1View.as_view(), name='user-type-list'),
    path('practice/signup/step3/<int:pk>',views.PracticeSignupStep3View.as_view(), name='practice-signup'),
    path('emergency-service/signup/step3/<int:pk>',views.EmergencyServiceSignupStep3View.as_view(), name='emergency-service-signup'),
    path('institution/signup/step3/<int:pk>',views.InstitutionSignupStep3View.as_view(), name='institution-signup'),
    
    path('emergency-services/step2/<int:pk>',views.EmergencyServiceStep2UpdateView.as_view(), name='select-emergency-service'),
    path('patient/signup/step2/',views.PatientSignupStep2View.as_view(), name='patient-signup'),
    path('insurance/signup/step2/<int:pk>',views.InsuranceProviderSignupStep2View.as_view(), name='insurance-provider-signup'),
    path('specialisation/step2/<int:pk>',views.SpecialisationStep2UpdateView.as_view(), name='select-specialisation'),
    path('institution/step2/<int:pk>',views.InstitutionStep2UpdateView.as_view(), name='institution-signup'),

]