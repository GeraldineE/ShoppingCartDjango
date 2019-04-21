from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.allProductCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug', views.ProdCatDetail, name='ProdCatDetail'),
]