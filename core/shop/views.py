from django.shortcuts import render
from .models import Product

# Create your views here.
def shop(request):
    product=Product.objects.all()
    context={'products':product}

    return render(request, 'shop.html',context)


def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')

def thankyou(request):
    return render(request,'thankyou.html')