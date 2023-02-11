from django.contrib import admin
from product import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','unit_price','quantity','description']
    list_editable=['unit_price']
    list_per_page=10
    search_fields=['title']
   
    



