from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
import string
from home.checkinput import Check
from django.contrib.auth.models import User
from home import db_functions


def index(request):
    global username
    if request.GET.get('log'):
        if Check.checkhomepage(Check, request.GET['uname'], request.GET['pword']):
            username = request.GET['uname']
            return HttpResponseRedirect('/userpage/')
        else:
            return render_to_response('homepage.html', {'error': Check.geterror(Check)})
    elif request.GET.get('sig'):
        return HttpResponseRedirect('/signup/')
    else:
        return render_to_response('homepage.html')


def getusername():
    return username


def gender(usr):
    if db_functions.homepgView(usr)['gender'] == 'm':
        return True
    if db_functions.homepgView(usr)['gender'] == 'M':
        return True

    return False
