from . import views
from django.urls import path
app_name = 'ecomapp'

urlpatterns = [
    path('', views.allProductCat, name='allProductCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='prod_Cat_Det')
]