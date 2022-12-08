from django.urls import path
from .views import show, Products


app_name = 'MyServ'

urlpatterns = [
    path('', show, name='index'),
    path('products/', Products.as_view(), name='product'),
]
