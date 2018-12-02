from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from home import db_functions
from home.checkinput import Check


def index(request):
    if request.GET.get('save'):
        if Check.checksignuppage(Check, request.GET['uname'], request.GET['pword'], request.GET['email'],
                                        request.GET['dob'], request.GET['gen']):
            db_functions.SubmitSignUp(request.GET['uname'], request.GET['pword'], '',
                                   request.GET['firstn'], request.GET['lastn'], request.GET['email'], '',
                                   request.GET['dob'], request.GET['gen'])
            return HttpResponseRedirect('http://cse442developers.com')
        else:
            return render_to_response('signup.html', {'error': Check.geterror(Check)})
    elif request.GET.get('cancel'):
        return HttpResponseRedirect('http://cse442developers.com')
    else:
        return render_to_response('signup.html')

