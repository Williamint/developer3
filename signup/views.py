from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from home import db_functions


def index(request):
    if request.GET.get('save'):
        db_functions.SubmitSignUp(request.GET['uname'], request.GET['pword'], '',
                                   request.GET['firstn'], request.GET['lastn'], request.GET['email'], '',
                                   request.GET['dob'], request.GET['gen'])
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    elif request.GET.get('cancel'):
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        return render_to_response('signup.html')

