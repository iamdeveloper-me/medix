from django.views import View
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from users.models import Profile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def stafflogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('/myadmin/dashboard/')
            else:
                messages.error(request, 'You are not authorized!')
    else:
        form = AuthenticationForm()
    return render(request, 'admin/staff_login.html', {'form': form})


class MyAdminDashboard(View):
    def get(self, request, *args, **kwargs):
        pateint     = Profile.objects.filter(custom_role__contains=0).count()
        practice    = Profile.objects.filter(custom_role__contains=1).count()
        institution = Profile.objects.filter(custom_role__contains=2).count()
        e_services  = Profile.objects.filter(custom_role__contains=3).count()
        h_providers = Profile.objects.filter(custom_role__contains=4).count()
        data = {
            "pateint"    : pateint,
            "practice"   : practice,
            "institution": institution,
            "e_services" : e_services,
            "h_providers": h_providers
        }
        return render(request, 'admin/staff_dashboard.html', data)


class AccountManagementView(View):
    def get(self, request, *args, **kwargs):
        account = Profile.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(account, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/account_management.html',data)


class PatientListingView(View):
    def get(self, request, *args, **kwargs):
        institution    = Profile.objects.filter(custom_role__contains=0)
        page = request.GET.get('page', 1)
        paginator = Paginator(institution, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/patient_listing.html',data)


class PracticeListingView(View):
    def get(self, request, *args, **kwargs):
        practice    = Profile.objects.filter(custom_role__contains=1)
        page = request.GET.get('page', 1)
        paginator = Paginator(practice, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/practice_listing.html',data)


class InstitutionListingView(View):
    def get(self, request, *args, **kwargs):
        institution    = Profile.objects.filter(custom_role__contains=2)
        page = request.GET.get('page', 1)
        paginator = Paginator(institution, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/institution_listing.html',data)


class EmergencyListingView(View):
    def get(self, request, *args, **kwargs):
        emergency    = Profile.objects.filter(custom_role__contains=3)
        page = request.GET.get('page', 1)
        paginator = Paginator(emergency, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/emergency_listing.html',data)


class InsuranceProvidersListingView(View):
    def get(self, request, *args, **kwargs):
        insurance = Profile.objects.filter(custom_role__contains=4)
        page = request.GET.get('page', 1)
        paginator = Paginator(insurance, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/insurance_listing.html',data)


def activate_user_ajax(request):
    try:
        profile_id = request.POST.get("profile_id")
        profile    = Profile.objects.get(pk=profile_id)
        user       = profile.user
        action_is  = request.POST.get("action_is") #activate/deactivate/pending

        if action_is == "activate":
            if profile.status == 0:
                #User is already Active. Raise Exception
                raise Exception("This Profile is already ACTIVE!!!")
            else:
                profile.status = 0
                profile.save()
                user.is_active = True
                user.save()
            res = {'status'  : 200,'message' : "Successfully Activated"}
        elif action_is == "pending":
            # For action_is = pending
            if profile.status == 1:
                #User is already in Pending Status. Raise Exception
                raise Exception("This Profile is already in PENDING!!!")
            else:
                profile.status = 1
                profile.save()
                user.is_active = False
                user.save()
                res = {'status'  : 200,'message' : "Changed to Pending!!"}
        else:
            # For action_is = deactivate
            if profile.status == 2:
                #User is already Deactive. Raise Exception
                raise Exception("This Profile is already DEACTIVATE!!!")
            else:
                profile.status = 2
                profile.save()
                user.is_active = False
                user.save()
                res = {'status'  : 200,'message' : "Successfully Deactivated!!!"}
        return JsonResponse(res)
    except Exception as e:
        res = {'status'  : 400,'message' : str(e)}
        return JsonResponse(res)
        

class StatisticsView(View):
    def get(self, request, *args, **kwargs):
        profiles     = Profile.objects.all()
        active_users    = profiles.filter(status=0).count()
        pending_users   = profiles.filter(status=1).count()
        deactive_users  = profiles.filter(status=2).count()
        data = {
            "active_users"   : active_users,
            "deactive_users" : deactive_users,
            "pending_users"  : pending_users
        }
        return render(request,'admin/statistics.html', data)


class ActiveAccountStatusView(View):
    def get(self, request, *args, **kwargs):
        user    = Profile.objects.filter(status=0)
        page = request.GET.get('page', 1)
        paginator = Paginator(user, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/active_status_listing.html',data)


class PendingStatusView(View):
    def get(self, request, *args, **kwargs):
        user    = Profile.objects.filter(status=1)
        page = request.GET.get('page', 1)
        paginator = Paginator(user, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/pending_status.html',data)


class DeactiveAccountStatusView(View):
    def get(self, request, *args, **kwargs):
        user    = Profile.objects.filter(status=2)
        page = request.GET.get('page', 1)
        paginator = Paginator(user, 2)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        data = {
            'users' : users
        }
        return render(request,'admin/deactive_status_listing.html',data)