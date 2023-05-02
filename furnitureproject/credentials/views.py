from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):

    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username):
                messages.info(request,"username is already taken")
                return redirect('signup')
            elif User.objects.filter(email=email):
                messages.info(request,"email is already taken")
                return redirect('signup')
            else:
                User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                return redirect('login')
        else:
            messages.info(request,"Invalid password")
            return redirect('signup')
    return render(request,"signup.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            user.save()
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('signup')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')