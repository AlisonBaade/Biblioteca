from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def home(request):
    if request.session.get('usuario'):
        return HttpResponse('Hello')   
    else:
        return redirect('/auth/login/?status=2')
