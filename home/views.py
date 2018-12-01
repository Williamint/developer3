from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
import string
from django.contrib.auth.models import User


def index(request):
    global username
    if request.GET.get('log'):
        if checkusername(request.GET['uname']) and checkpassword(request.GET['pword']):
            #usname = User.objects.create_user(request.GET['uname'], '', '')
            #usname.save()
            #username = usname
            #User().username = request.GET['uname']
            username = request.GET['uname']
            return HttpResponseRedirect('/userpage/')
        else:
            return render_to_response('homepage.html', {'error': 'You have invalid password'})
    elif request.GET.get('sig'):
        return HttpResponseRedirect('/signup/')
    else:
        return render_to_response('homepage.html')


def getusername():
    return username


def checkusername(uname):
        if len(uname) >= 12 or len(uname) == 0:
            return False
        elif any(c in uname for c in('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
            return False
        elif any(c in uname for c in string.punctuation):
            return False
        else:
            return True


def checkpassword(pword):
    if len(pword) > 16 or len(pword) < 8:
        return False
    elif any(c in pword for c in string.punctuation):
        return False
    elif not any(c.isupper() for c in pword):
        return False
    elif not any(c.islower() for c in pword):
        return False
    elif not any(c.isdigit() for c in pword):
        return False
    else:
        return True
