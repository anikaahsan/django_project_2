from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.IntegerField()
    

    def __str__(self) -> str:
        return self.title