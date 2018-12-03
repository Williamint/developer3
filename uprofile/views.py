from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from home.checkinput import Check
from home import db_functions
from home import views


def index(request):

    if request.GET.get('bth'):
        return HttpResponseRedirect('/userpage/')

    if request.GET.get('save'):
        if Check.checkeditpage(Check, request.GET['email'], request.GET['bith']):
            db_functions.editProfile(views.getusername(), request.GET['firstn'], request.GET['lastn'],
                                     request.GET['email'], request.GET['bith'], request.GET['education'])
            return HttpResponseRedirect('/userpage/')
        else:
            dictP = db_functions.homepgView(views.getusername())
            return render_to_response('userprofiles.html', {'errormsg': Check.geterror(Check),
                                                        'firstna': dictP['firstname'],
                                                        'lastna': dictP['lastname'],
                                                        'emailv': dictP['email'],
                                                        'eduv': dictP['education'],
                                                        'birth': dictP['dateofbirth']
                                                        })

    dictP = db_functions.homepgView(views.getusername())
    return render_to_response('userprofiles.html', {'firstna': dictP['firstname'],
                                                    'lastna': dictP['lastname'],
                                                    'emailv': dictP['email'],
                                                    'eduv': dictP['education'],
                                                    'birth': dictP['dateofbirth']
                                                   })
