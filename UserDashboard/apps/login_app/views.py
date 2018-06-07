from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string

from .models import User
import bcrypt
#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
# Create your views here.
def index(request):
    return render(request,'login_app/index.html')

def loginreg(request):
    return render(request,'login_app/login.html')

def registration(request):
    return render(request,'login_app/register.html')

def register(request):
    print "entered register!"
    errors = User.objects.data_validator_registration(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/registration')

    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        User.objects.create(first_name=request.POST['f_name'], last_name=request.POST['l_name'], email =request.POST['email'], password=hashed_pw)
        inserted_user = User.objects.last()
        id = inserted_user.id
        request.session['user_data']={
        "id" : id,
        "first_name":request.POST['f_name'],
        "last_name" : request.POST['l_name'],
        "level_id":2
        }
        request.session['type'] = 'registered'

        return redirect('/success')
def login(request):
    errors = User.objects.data_validator_login(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/loginreg')
    else:
        user = User.objects.filter(email=request.POST['email'])
        request.session['user_data']={
        "id" : user[0].id,
        "first_name":user[0].first_name,
        "last_name" : user[0].last_name,
        "level_id":user[0].level_id
        }
        request.session['type'] = 'logged in'
        return redirect('/success')

def success(request):
    return redirect('/dashboard')
