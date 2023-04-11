from django.urls import path
from . import shop_views

urlpatterns =[
    path('', shop_views.shop, name='shophome')
]
