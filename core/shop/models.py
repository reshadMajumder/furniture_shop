from django.db import models

# Create your models here.
class Product(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50,null=False)
    price=models.FloatField(null=False)

    def __str__(self):
        return self.name
    