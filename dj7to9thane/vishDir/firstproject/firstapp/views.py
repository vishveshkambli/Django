from django.shortcuts import render, HttpResponse
ulist=[]

# Create your views here.

def homef(request):
    return render(request,'home.html')

def firstpage(request):
    return render (request,'first.html')

def secondpage(request):
    return render (request,'second.html')

def adduser(request):
    return render(request,'adduser.html')

def Add_User(request):
    id=request.GET.get('fname')
    name=request.GET.get('lname')
    t=(id,name)
    return HttpResponse('<h1>Success'+str(t)+' </h1>')

def adduser2(request):
    return render(request,'adduser2.html')

def Add_User2(request):
    id=request.POST.get('fname')
    name=request.POST.get('lname')
    t=(id,name)
    ulist.append(t)
    return render(request,'home.html')

def userlist(request):
    return render(request,'ulist.html',{'l':ulist})