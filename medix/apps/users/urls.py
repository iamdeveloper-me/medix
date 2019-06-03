from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),

    #user dashboard
    path('dashboard/practice/<int:pk>',views.PracticeDashboardView.as_view(), name='practice-dashboard'),
    path('dashboard/institution/',views.InstitutionDashboardView.as_view(), name='institution-dashboard'),
    path('dashboard/emergency-service/',views.EmergencyServicesDashboard.as_view(), name='emergency-service-dashboard'),
    path('dashboard/emergency-service/',views.EmergencyServicesDashboard.as_view(), name='admin-dashboard'),
    path('dashboard/health-insurance/',views.HealthInsuranceDashboard.as_view(), name='health-insurance-dashboard'),

    #admin dashboard
    path('admin/dashboard/',views.AdminDashboardView.as_view(), name='admin-dashboard'),

    path('logout/',views.LogoutView.as_view(), name='users-logout'),
    path('user/login/',views.LoginView.as_view(), name='users-login'),



    path('user-type/step1/',views.UserTypeStep1View.as_view(), name='registration-step1'),



    path('practice/signup/step3/<int:pk>',views.PracticeSignupStep3View.as_view(), name='practice-signup'),
    path('emergency-service/signup/step3/<int:pk>',views.EmergencyServiceSignupStep3View.as_view(), name='emergency-service-signup'),
    path('institution/signup/step3/<int:pk>',views.InstitutionSignupStep3View.as_view(), name='institution-signup'),
    

    path('emergency-services/step2/',views.EmergencyServiceStep2CreateView.as_view(), name='select-emergency-service'),
    path('patient/signup/step2/',views.PatientSignupStep2View.as_view(), name='patient-signup'),
    path('insurance/signup/step2/',views.InsuranceProviderSignupStep2View.as_view(), name='insurance-provider-signup'),
    path('practice/step2/',views.PracticeStep2CreateView.as_view(), name='select-specialisation'),
    path('institution/step2/',views.InstitutionStep2CreateView.as_view(), name='institution-step2'),


    # path('practice/step1/',views.PracticeStep1CreateView.as_view(), name='practice-step1'),
    path('form/submit/',views.UserFormSubmitView.as_view(), name='form-submit'),

    #dashboard details form
    # path('user/profile/',views.profile_info, name='user-profile'),

    
    path('create/overview/<int:pk>',views.ProfessionalOverviewUpdate.as_view(), name='professional-overview'),

    path('profile/detail/<int:pk>',views.PracticeInfoDetailView.as_view(), name='profile-information'),
    path('professional/detail/<int:pk>',views.ProfessionalOverviewDetail.as_view(), name='professional-detail'),
    
    path('price/<int:pk>',views.PriceUpdateView.as_view(), name='price'),
    
    path('price/detail/<int:pk>',views.PriceDetail.as_view(), name='price-detail'),
    
]