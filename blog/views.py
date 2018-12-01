from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
#from library.usermodel import User
#from library import databasecheck
from home import views
from home import db_functions


def index(request):
    if request.GET.get('bth'):
        return HttpResponseRedirect('/userpage/')
    if request.GET.get('share'):
        return render_to_response('blog.html', {'pname': views.getusername(), 'msg_lists': db_functions.adduserstory(views.getusername(), views.getusername()+": "+request.GET['story'])})

    msg_list = db_functions.userstory(views.getusername())
    print(msg_list)
    return render_to_response('blog.html', {'pname': views.getusername(), 'msg_lists': msg_list})
