from django.shortcuts import render,redirect
from .models import Product,Cart,CartItem

# Create your views here.
def shop(request):
    product=Product.objects.all()
    context={'products':product}

    return render(request, 'shop.html',context)


def cart(request):
    cart_products_details=CartItem.objects.all()
    context={'products':cart_products_details}
    return render(request,'cart.html',context)

def _cart_id(request): #get the session id for making the cart id
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()

    return cart

def add_to_cart(request, product_id):
    product=Product.objects.get(id=product_id) #get the product
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) #get the cart using the cart id present in the sessiom
    except Cart.DoesNotExist:
        cart= Cart.objects.create(
            cart_id=_cart_id(request)
            )
    cart.save()

#lets combile product and cart  to get many product in one cart
    
    try:
        cart_item=CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product = product ,
            cart=cart,
            quantity = 1,

        )
        cart_item.save()
    return redirect('shop')


def checkout(request):
    return render(request,'checkout.html')

def thankyou(request):
    return render(request,'thankyou.html')