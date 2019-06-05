from django.http import  JsonResponse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from .models import Profile, Education, Product, Location 
from django.contrib.auth.models import User
# from .forms import CreateExpertiseForm


def edit_profile(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        user = User.objects.get(id=profile.user.id)
        profile.phone = request.POST.get("phone")
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
            # education.qualification = request.POST.get("qualification")
            # education.user = user
            # education.save()
        except Exception as e:
            Education.objects.create(user=user,qualification=request.POST.get("qualification"))
        return JsonResponse({'status':200}) 

def add_product(request):
    profile = Profile.objects.get(id=request.POST.get("profile_id"))
    user = User.objects.get(id=profile.user.id)
    try:
        product = Product.objects.filter(user=user)
        Product.objects.create(user=user,item=request.POST.get("item"),price=request.POST.get("price"))
    except Exception as e:
        Product.objects.create(user=user,item=request.POST.get("item"),price=request.POST.get("price")) 
    return JsonResponse({'status':200}) 


def edit_education(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
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
        product.save()
        return JsonResponse({'status':200})

def add_location(request):
    if request.method == 'POST':
        
        profile = Profile.objects.get(id=request.POST.get("profile_id"))
        user = User.objects.get(id=profile.user.id)
        try:
            location = Location.objects.get(user=user)
            Location.objects.create(user=user,location=request.POST.get("location"))
        except Exception as e:
            Location.objects.create(user=user,location=request.POST.get("location"))
        return JsonResponse({'status':200}) 