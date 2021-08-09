from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User, auth

def authlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials')
            return redirect('login')
    else:        
        return render(request,'authentication/login.html')

def authregistration(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username Already Exists')
                return redirect('registration')    
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=fname,last_name=lname)
                user.save();
                messages.success(request,'Registration Successfully Done!')
                return redirect('login')
        else:
            messages.error(request, 'Password not matched')
            return redirect('registration')
    else:
        return render(request,'authentication/registration.html')
def authforgotpassword(request):
    return render(request,'authentication/forgot.html')

def logout(request):
    auth.logout(request)
    return redirect('/')