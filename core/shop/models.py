from django.db import models

# Create your models here.
class Product(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50,null=False)
    price=models.FloatField(null=False)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    cart_id=models.CharField(max_length=300,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def total(self):
        return self.quantity * self.product.price


    def __str__(self):
        return self.product.name