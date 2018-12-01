from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

from django.shortcuts import render_to_response, render
from home import views
from django.http import HttpResponseRedirect


def index(request):
    if request.GET.get('msg'):
        return HttpResponseRedirect('/groupchat/')
    if request.GET.get('blog'):
        return HttpResponseRedirect('/blog/')
    if request.GET.get('sigt'):
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    if request.GET.get('edit'):
        return HttpResponseRedirect('/userprofile/')
    if request.GET.get('friend'):
        return HttpResponseRedirect('/friend/')

    return render(request, 'userpage.html', {'nickname': views.getusername()})
