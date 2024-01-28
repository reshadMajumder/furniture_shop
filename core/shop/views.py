from django.shortcuts import render,redirect
from .models import Product,Cart,CartItem

# Create your views here.
def shop(request):
    product=Product.objects.all()
    context={'products':product}

    return render(request, 'shop.html',context)


def cart(request,total=0,quantity=0,cart_items=None ):
    try:
       
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,is_active=True)

        for cart_item in cart_items:
            total+=int(cart_item.price)*int(cart_item.quantity)
            quantity+=int(cart_item.quantity)
        
    except:
        pass


    context={
            'cart_items':cart_items,
            'total':total,
            'quantity':quantity
             }
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

def add_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
        cart_item.save()

    return redirect('cart')

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        # If the cart doesn't exist, nothing to remove
        return redirect('cart')

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        # If the cart item doesn't exist, nothing to remove
        pass

    return redirect('cart')




def checkout(request):
    return render(request,'checkout.html')

def thankyou(request):
    return render(request,'thankyou.html')







"""
please ignore this 
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product, Cart, CartItem

def cart(request):
    cart = get_or_create_cart(request)
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    total = sum(item.product.price * item.quantity for item in cart_items)
    quantity = sum(item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
        'quantity': quantity
    }
    return render(request, 'cart.html', context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def get_or_create_cart(request):
    cart_id = _cart_id(request)
    cart, created = Cart.objects.get_or_create(cart_id=cart_id)
    return cart

def add_or_update_cart_item(request, product_id, increment=True):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if increment:
            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(product=product, cart=cart, quantity=1)

    return redirect('shop')

def add_to_cart(request, product_id):
    return add_or_update_cart_item(request, product_id, increment=True)

def remove_from_cart(request, product_id):
    return add_or_update_cart_item(request, product_id, increment=False)

"""