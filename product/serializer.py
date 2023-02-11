from rest_framework import serializers
from .models import Product


# class ProductSerializer(serializers.ModelSerializer):
#     id=serializers.IntegerField(source='pk')
#     #title=serializers.CharField(max_length=100)
#    # description=serializers.CharField(max_length=250)
#    # unit_price=serializers.DecimalField(max_digits=6,decimal_places=2)
#    # quantity=serializers.IntegerField()
#     class Meta:
#       model=Product
#       fields=['id','title','description','unit_price','quantity']

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'