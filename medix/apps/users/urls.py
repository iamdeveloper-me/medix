from django.urls import path
from users import views
from .ajax import * 

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),

    #user dashboard
    path('edit/profile/<int:pk>',views.PracticeUpdateView.as_view(), name='edit-practice'),
    path('dashboard/institution/',views.InstitutionDashboardView.as_view(), name='institution-dashboard'),
    path('dashboard/emergency-service/',views.EmergencyServicesDashboard.as_view(), name='emergency-service-dashboard'),
    path('dashboard/emergency-service/',views.EmergencyServicesDashboard.as_view(), name='admin-dashboard'),
    path('dashboard/health-insurance/',views.HealthInsuranceDashboard.as_view(), name='health-insurance-dashboard'),

    #admin dashboard
    path('admin/dashboard/',views.AdminDashboardView.as_view(), name='admin-dashboard'),

    path('logout/',views.LogoutView.as_view(), name='users-logout'),
    path('user/login/',views.LoginView.as_view(), name='users-login'),


    #signup step first
    path('user-type/step1/',views.UserTypeStep1View.as_view(), name='registration-step1'),


    #signup step third
    path('practice/signup/step3/<int:pk>',views.PracticeSignupStep3View.as_view(), name='practice-signup'),
    path('emergency-service/signup/step3/<int:pk>',views.EmergencyServiceSignupStep3View.as_view(), name='emergency-service-signup'),
    path('institution/signup/step3/<int:pk>',views.InstitutionSignupStep3View.as_view(), name='institution-signup'),
    
    #signup step second
    path('emergency-services/step2/',views.EmergencyServiceStep2CreateView.as_view(), name='select-emergency-service'),
    path('patient/signup/step2/',views.PatientSignupStep2View.as_view(), name='patient-signup'),
    path('insurance/signup/step2/',views.InsuranceProviderSignupStep2View.as_view(), name='insurance-provider-signup'),
    path('practice/step2/',views.PracticeStep2CreateView.as_view(), name='select-specialisation'),
    path('institution/step2/',views.InstitutionStep2CreateView.as_view(), name='institution-step2'),


    # path('practice/step1/',views.PracticeStep1CreateView.as_view(), name='practice-step1'),
    path('form/submit/',views.UserFormSubmitView.as_view(), name='form-submit'),

    
    path('create/overview/<int:pk>',views.ProfessionalOverviewUpdate.as_view(), name='professional-overview'),

    path('profile/detail/<int:pk>',views.PracticeInfoDetailView.as_view(), name='profile-information'),
    path('professional/detail/<int:pk>',views.ProfessionalOverviewDetail.as_view(), name='professional-detail'),
    
    # path('create/product/<int:pk>',views.ProductCreateView.as_view(), name='create-product'),
    
    # path('price/detail/<int:pk>',views.PriceDetail.as_view(), name='price-detail'),

    path('create/education/',views.EducationCreateView.as_view(), name='create-education'),
    
    path('education/detail/<int:pk>',views.EducationDetailView.as_view(), name='education-detail'),

    path('dashboard/practice/<int:pk>',views.PracticeProfileDetailView.as_view(), name='profile-dashboard')
]

ajaxpatterns = [
    path('add/location', add_location, name='add-location'),
    path('edit/profile/', edit_profile, name='edit-profile'),
    path('add/statement', add_statement, name='add-statement'),
    path('add/education', add_education, name='add-education'),
    
    path('add/product', add_product, name='add-product'),
    path('edit/education', edit_education, name='edit-education'),
    path('edit/product', edit_product, name='edit-product'),
    
    path('add/keyword', add_keyword, name='add-keyword'),
    path('delete/education', delete_education, name='qualification-delete'),
    path('delete/product', delete_product, name='product-delete'),
       

]    

urlpatterns = urlpatterns + ajaxpatterns