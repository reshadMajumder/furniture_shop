from django.urls import path,include
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
    path('cart',cart,name='cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart, name="add_to_cart"),

    path('checkout/',checkout,name='checkout'),
    path('thankyou/',thankyou,name='thankyou'),

]
