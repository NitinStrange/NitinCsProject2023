from collections import UserDict
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
import csv
x='bruh -_-'


def signup(request):
    if request.method == 'POST':
        UsName=request.POST['UserName']
        Email=request.POST['Email']
        Fname=request.POST['FirstName']
        Lname=request.POST['LastName']
        PsWord=request.POST['Pass1']
        CPsWord=request.POST['Pass2']
        #myuser=User.objects.create()
        if PsWord==CPsWord:
            f=open('db.csv','w')
            w=csv.writer(f)
            #v=([UsName,Email,Fname,Lname,PsWord])
            w.writerow([UsName,Email,Fname,Lname,PsWord])
            f.close()
            return render(request, 'signin.html')
        else:
            messages.error(request, "Failed")
            return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        UsName=request.POST['UserName']
        PsWord=request.POST['PassWord']
        f=open('db.csv','r')
        data=csv.reader(f)
        for i in data:
            if i[0]==UsName:
                if i[4]==PsWord:
                    fname=i[2]
                    return render(request, 'ui2.html',{'fname':fname})
    return render(request,'signin.html')


def home(request):
    return render(request,'ui2.html', {'summa':x})

def admins(request):
    return render(request,'admin.html')

def pg2_1(request):
    return render(request,'2ndpage1.html')

def pg2_2(request):
    return render(request,'2ndpage2.html')

def pg2_3(request):
    return render(request,'2ndpage3.html')

def pg2_4(request):
    return render(request,'2ndpage4.html')

def pg3(request):
    return render(request,'3rdpage.html')