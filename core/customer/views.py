from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django .contrib.auth import authenticate,login,logout
from django .contrib.auth import login as auth_login
from django.contrib import messages


# Create your views here.



def signup(request):
    if request.method=='POST':
        data=request.POST

        username=data.get('username')
        email=data.get('email')
        mobile=data.get('mobile')
        password=data.get('password')

        users=User.objects.create_user(username, email, password)
        users.mobile=mobile
        users.save()
        messages.success(request,"sign up successfull")
        return redirect('login')



    return render(request, 'signup.html')

def handlelogin(request):
    if request.method ==  "POST":
        data=request.POST

        username=data.get('username')
        password=data.get('password')


        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            print("logged in")
           
            return redirect('home')
        
        
        
        else:
            messages.error(request,'Username or Password is incorrect')
            print("not in")

            return redirect('login')

    return render(request,'login.html')


def handlelogout(request):
    logout(request)
    return redirect('home')
