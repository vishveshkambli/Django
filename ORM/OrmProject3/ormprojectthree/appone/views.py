from django.shortcuts import render, HttpResponse, redirect
userlist=[]
# Create your views here.
from .models import Manual

def homef(request):
    return render (request,'home.html')

def page1f(request):
    return render (request,'page1.html')

def Page1F(request):
    id=request.GET.get('fname')
    name=request.GET.get('lname')
    t=(id,name)
    return HttpResponse('<h1>success'+str(t)+'</h1>')

def page2f(request):
    return render (request,'page2.html')

def Page2F(request):
    id=request.POST.get('fname')
    name=request.POST.get('lname')
    t=(id,name)
    userlist.append(t)
    return render (request,'home.html')

def userlistf(request):
    return render(request, 'userlist.html',{'l':userlist})

def postmanualf(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        m=Manual()
        m.name=name
        m.email=email
        m.save()
        return redirect('/')
    else:
        return render (request, 'postmanual.html')

from .form import AutoForm

def postautof(request):
    if request.method=='POST':
        a=AutoForm(request.POST)
        a.save()
        return redirect('/')
    else:
        a=AutoForm
        d={'form':a}
        return render(request, 'postauto.html',d)
