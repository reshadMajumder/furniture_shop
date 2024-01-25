from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def login(request):
    return render(request, 'login.html')


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
        return redirect('signup')



    return render(request, 'signup.html')