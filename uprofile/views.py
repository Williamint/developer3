from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect

def index(request):
    if request.GET.get('bth'):
        return HttpResponseRedirect('/userpage/')

    return render_to_response('userprofiles.html')
