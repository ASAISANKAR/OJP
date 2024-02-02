from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='logout')
def projecthomepage(request):
    return render(request,'adminmodulehomepage.html')

def signup(request):
    return render(request,'signup.html')

def signup1(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken.')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created Successfully!')
                return render(request,'adminmodulehomepage.html')

        else:
            messages.info(request, 'Password does not match.')
            return render(request, 'signup.html')

def login(request):
    return render(request,'login.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                return render(request,'jobseekerhomepage.html')
            elif len(username)==4:
                return render(request,'employerhomepage.html')
            else:
                return render(request,'adminmodulehomepage.html')

        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return render(request,'adminmodulehomepage.html')

