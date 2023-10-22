from django.shortcuts import render, HttpResponse
userlist=[]
# Create your views here.

def homef(request):
    return render(request, 'home.html')

def getf(request):
    return render(request, 'get.html')

def GetF(request):
    id=request.GET.get('fname')
    name=request.GET.get('lname')
    t=(id,name)
    return HttpResponse ('</h1>success'+str(t)+'</h1>')

def postf(request):
    return render(request, 'post.html')

def PostF(request):
    id=request.POST.get('fname')
    name=request.POST.get('lname')
    t=(id,name)
    userlist.append(t)
    return render(request, 'home.html')

def UserListF(request):
    return render(request, 'userlist.html',{'l':userlist})
    
