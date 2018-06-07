from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import localtime, strftime
from datetime import datetime
from django.utils.crypto import get_random_string
from .models import *
import bcrypt

def index(request):
    user = User.objects.all()
    user_details = user.values('id','first_name','last_name','email','created_at','level_id__level')
    print user_details
    context={
        'user' : user_details
    }
    return render(request,'dashboard_app/index.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')
