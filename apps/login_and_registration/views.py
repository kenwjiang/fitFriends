from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User, Gym
import bcrypt


def index(request):
    return render(request, 'login_and_registration/index.html')

def create(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, key)
        # return redirect('/login')
        return render(request, 'login_and_registration/reg_errors.html')

    placeholder = Gym.objects.create(place_id = 'placeholder')
    pw = bcrypt.hashpw(request.POST['reg-password'].encode(), bcrypt.gensalt())
    new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],dob=request.POST['dob'], gender=request.POST['reg_gender'], email = request.POST['email'],def_gym=placeholder, password=pw)
    request.session['first_name'] = request.POST['first_name']
    request.session['user_id'] = new_user.id
    print(new_user.id)
    return redirect('/login/success')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value, key)
        return redirect('/login')
    user = User.objects.filter(email=request.POST['log-email'])
    request.session['first_name'] = user[0].first_name
    request.session['user_id'] = user[0].id
    return redirect('/login/success')

def success(request):
    if 'first_name' not in request.session:
        messages.error(request, 'You are not the correct user.')
        return redirect('/login')
    return redirect('/dashboard')

def logout(request):
    del request.session['first_name']
    del request.session['user_id']
    return redirect('/login')
