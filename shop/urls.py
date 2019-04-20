from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.allProductCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
]