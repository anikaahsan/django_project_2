from django.urls import path
from product import views
from product.genericview import ProductsCreateAndListView


urlpatterns = [
    path('product/', views.product_list),
       path('product/<int:id>',views.product_detail),
       path('g/prodcts/', ProductsCreateAndListView.as_view())
]
