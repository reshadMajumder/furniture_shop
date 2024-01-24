from django.urls import path,include
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
    path('cart',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('thankyou/',thankyou,name='thankyou'),

]
