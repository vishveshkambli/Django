from django.shortcuts import render, HttpResponse
userlist=[]

# Create your views here.
def homeF(request):
    return render(request,'home.html')

def adduser1f(request):
    return render(request, 'adduser1.html')

def AddUser1F(request):
    id=request.GET.get('fname')
    name=request.GET.get('lname')
    t=(id,name)
    return HttpResponse('<h1>Success'+str(t)+'</h1>')

def adduser2f(request):
    return render(request, 'adduser2.html')

def AddUser2F(request):
    id=request.POST.get('fname')
    name=request.POST.get('lname')
    t=(id,name)
    userlist.append(t)
    return render(request,'home.html')

def UserListF(request):
    return render(request, 'userlist.html',{'l':userlist})


    
