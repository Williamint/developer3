from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from home import db_functions
from home import views


def index(request):
    global sfriendn
    if request.GET.get('bth'):
        return HttpResponseRedirect('/userpage/')

    if request.GET.get('add'):
        if db_functions.addFriend(views.getusername(), request.GET['search']):
            return render(request, 'friends.html', {'friend_list': db_functions.getFriend(views.getusername())})
        else:
            return HttpResponseRedirect('/friend/')

    if request.GET.get('friendB'):
        sfriendn = request.GET['friendB']
        msg_list = db_functions.getuserstory(sfriendn)
        dictF = db_functions.homepgView(sfriendn)
        return render_to_response('friend_blog.html', {'pname': request.GET['friendB'], 'gender': views.gender(sfriendn),
                                    'msg_lists': msg_list, 'currentuser': views.getusername(),
                                    'fn': dictF['firstname'], 'ln': dictF['lastname'], 'mail': dictF['email'],
                                    'dob': dictF['dateofbirth'], 'edu': dictF['education'],
                                        'friend_list': db_functions.getFriend(sfriendn)})

    if request.GET.get('share'):
        msg_list = db_functions.adduserstory(sfriendn, views.getusername()+": "+request.GET['story'])
        dictF = db_functions.homepgView(sfriendn)
        return render_to_response('friend_blog.html',
                                  {'pname': sfriendn, 'gender': views.gender(sfriendn),
                                   'msg_lists': msg_list, 'fn': dictF['firstname'], 'ln': dictF['lastname'], 'mail': dictF['email'],
                                    'dob': dictF['dateofbirth'], 'edu': dictF['education'],
                                        'friend_list': db_functions.getFriend(sfriendn)})
    if request.GET.get('btf'):
        return render_to_response('friends.html', {'friend_list': db_functions.getFriend(views.getusername())})

    return render_to_response('friends.html', {'friend_list': db_functions.getFriend(views.getusername())})


def getfriendn():
    return sfriendn
