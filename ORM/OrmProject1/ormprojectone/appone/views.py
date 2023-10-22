from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import Emp

def homef(request):
    return render(request,'home.html')

def addempf(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        age=request.POST.get('age')
        address=request.POST.get('address')
        e=Emp()
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect('/')
    else:
        return render(request,'addemp.html')


    

