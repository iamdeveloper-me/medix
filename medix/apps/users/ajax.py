from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from .models import Profile, Education, Product, Location, OperatingHours, AmbulanceService, Keywords
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse

def edit_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        user = User.objects.get(id=profile.user.id)
        profile.phone = request.POST.get("phone")
        profile.gender = request.POST.get("gender")
        profile.save()
        user.first_name = request.POST.get("firstName")
        user.last_name = request.POST.get("lastName")
        user.save()
        return JsonResponse({'status':200}) 

def add_statement(request):  
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        profile.description = request.POST.get("description")
        profile.experience = request.POST.get("experience")
        profile.save()
        return JsonResponse({'status':200}) 

def add_education(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        user = User.objects.get(id=profile.user.id)
        try:
            education = Education.objects.get(user=user)
            Education.objects.create(user=user,qualification=request.POST.get("qualification"))
        except Exception as e:
            Education.objects.create(user=user,qualification=request.POST.get("qualification"))
        return JsonResponse({'status':200}) 

def add_product(request):
    # import pdb; pdb.set_trace()
    profile = Profile.objects.get(id=request.POST.get("profile_id"))
    user = User.objects.get(id=profile.user.id)
    try:
        product = Product.objects.filter(user=user)
        Product.objects.create(user=user,item=request.POST.get("item"),price=request.POST.get("price"),on_request=request.POST.get("onRequest").title())
    except Exception as e:
        Product.objects.create(user=user,item=request.POST.get("item"),price=request.POST.get("price"),on_request=request.POST.get("onRequest")) 
    return JsonResponse({'status':200}) 


def edit_education(request):
    if request.method == 'POST':
        edu = Education.objects.get(id=request.POST.get("edu_id"))
        user = User.objects.get(id=edu.user.id)
        edu.qualification = request.POST.get("qualification")
        edu.user = user
        edu.save()
        return JsonResponse({'status':200})

def edit_product(request):
    if request.method == 'POST':
        product = Product.objects.get(id=request.POST.get("product_id"))
        product.item = request.POST.get("item")
        product.price = request.POST.get("price")
        product.on_request = request.POST.get("onRequest").title()
        product.save()
        return JsonResponse({'status':200})

def add_keyword(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        keyword = Keywords.objects.create(user=profile.user,keyword=request.POST.get("keyword"))
        return JsonResponse({'status':200})

def delete_education(request):
    education = Education.objects.get(pk=request.GET.get('education_id'))
    education.delete()
    return JsonResponse({'status':200})

def delete_product(request):
    product = Product.objects.get(pk=request.GET.get('product_id'))
    product.delete()
    return JsonResponse({'status':200})

def edit_insurance_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        user = User.objects.get(id=profile.user.id)
        profile.phone = request.POST.get("phone")
        profile.contact_person = request.POST.get("contactp")
        profile.address_of_institution = request.POST.get("address")
        profile.trading_name = request.POST.get("trad_name")
        profile.save()
        return JsonResponse({'status':200})

def add_ambulance_info(request):
    profile = Profile.objects.get(id=request.POST.get("profile_id"))
    user = User.objects.get(id=profile.user.id)
    try:
        AmbulanceService.objects.create(user=user,location=request.POST.get("location"),contact=request.POST.get("contact"))
    except Exception as e:
        AmbulanceService.objects.create(user=user,location=request.POST.get("location"),contact=request.POST.get("contact"))
    return JsonResponse({'status':200})

def edit_ambulance_info(request):
    if request.method == 'POST':
        ambulance = AmbulanceService.objects.get(id=request.POST.get("ambulance_id"))
        ambulance.location = request.POST.get("locationInfo")
        ambulance.contact = request.POST.get("contact")
        ambulance.save()
        return JsonResponse({'status':200})

def ambulance_info_delete(request):
    ambulance = AmbulanceService.objects.get(pk=request.GET.get('ambulance_id'))
    ambulance.delete()
    return JsonResponse({'status':200})

def add_insurance_overview(request):
    add_statement(request)
    return JsonResponse({'status':200})

def add_insurance_product(request):
    add_product(request) 
    return JsonResponse({'status':200}) 

def insurance_product_delete(request):
    delete_product(request)
    return JsonResponse({'status':200})

def edit_insurance_product(request):
    edit_product(request)
    return JsonResponse({'status':200})

def add_insurance_keyword(request):
    add_keyword(request)
    return JsonResponse({'status':200})

def delete_keyword(request):
    keyword = Keywords.objects.get(id=request.GET.get("keyword_id"))
    keyword.delete()
    return JsonResponse({'status':200})

def delete_description(request):
    profile = Profile.objects.filter(id=request.GET.get("profile_id")).update(description=None)
    return JsonResponse({'status':200})

def delete_experience(request):
    profile = Profile.objects.filter(id=request.GET.get("profile_id")).update(experience=None)
    return JsonResponse({'status':200})

#ajax for login page
def login_form(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        role = Profile.objects.filter(user_id=user.id)
        return role,user
    return False

def practice_login(request):
    if login_form(request) != False:
        role,user = login_form(request)
        if role[0].custom_role==1 and user.is_active and user.is_staff==False:
            login(request, user)
            return JsonResponse({'status':200,'user_id':request.user.profile.id})
    return JsonResponse({'status':400})

def institution_login(request):
    if login_form(request) != False:
        role,user = login_form(request)
        if role[0].custom_role==2 and user.is_active and user.is_staff==False:
            login(request, user)
            return JsonResponse({'status':200,'user_id':request.user.profile.id})
    return JsonResponse({'status':400})

def service_login(request):
    if login_form(request) != False:
        role,user = login_form(request)
        if role[0].custom_role==3 and user.is_active and user.is_staff==False:
            login(request, user)
            return JsonResponse({'status':200,'user_id':request.user.profile.id})
    return JsonResponse({'status':400})

def insurance_login(request):
    if login_form(request) != False:
        role,user = login_form(request)
        if role[0].custom_role==4 and user.is_active and user.is_staff==False:
            login(request, user)
            return JsonResponse({'status':200,'user_id':request.user.profile.id})
    return JsonResponse({'status':400})

def patient_login(request):
    if login_form(request) != False:
        role,user = login_form(request)
        if role[0].custom_role==0 and user.is_active and user.is_staff==False:
            login(request, user)
            return JsonResponse({'status':200,'user_id':request.user.profile.id})
    return JsonResponse({'status':400})

def delete_location(request):
    location = Location.objects.get(pk=request.GET.get('location_id'))
    location.delete()
    return JsonResponse({'status':200})

def add_location(request):
    if request.method == 'POST':
        profile = Profile.objects.get(id=request.POST.get("profile_id"))

        user = profile.user
        day_list = []
        day_list.append(request.POST.get('monday'))
        day_list.append(request.POST.get('tueday'))
        day_list.append(request.POST.get('wedday'))
        day_list.append(request.POST.get('thuday'))
        day_list.append(request.POST.get('friday'))
        day_list.append(request.POST.get('satday'))

        open_list = []
        open_list.append(request.POST.get('monopn'))
        open_list.append(request.POST.get('tueOpn'))
        open_list.append(request.POST.get('wedOpn'))
        open_list.append(request.POST.get('thuOpn'))
        open_list.append(request.POST.get('friOpn'))
        open_list.append(request.POST.get('satOpn'))

        close_list = []
        close_list.append(request.POST.get('monclos'))
        close_list.append(request.POST.get('tueCls'))
        close_list.append(request.POST.get('wedCls'))
        close_list.append(request.POST.get('thuCls'))
        close_list.append(request.POST.get('friCls'))
        close_list.append(request.POST.get('satCls'))

        location_obj = Location.objects.create(user=user,location=request.POST.get("locations"))
        try:
            for day, openl, closel in zip(day_list,open_list,close_list):
                OperatingHours.objects.create(
                    open_time=openl,
                    close_time=closel,
                    day=day,
                    location=location_obj
                )

            return JsonResponse({'status':200}) 
        except Exception as e:
            print("Uh oh, Error : ", str(e))
            return JsonResponse({'status':200}) 
    return JsonResponse({'status':400}) 
 
def edit_location(request):
    loc_hour_list=[]
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        location_obj = Location.objects.get(id=request.POST.get("location_id"))
        tradHour_obj = OperatingHours.objects.filter(location=location_obj)
        loc_hour_list = [{
            'pk'        : hour.pk,
            'open_time' : hour.open_time,
            'close_time': hour.close_time,
            'day'       : hour.day,
            'location'  : hour.location.id
        } for hour in tradHour_obj]
        return JsonResponse({'status':200,'loc_hour_list':loc_hour_list}) 
    return JsonResponse({'status':400}) 
 

