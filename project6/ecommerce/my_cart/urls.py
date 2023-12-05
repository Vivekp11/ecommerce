from . import views
from django.urls import path
app_name = 'my_cart'

urlpatterns = [
    path('', views.prodDetail, name='prod_Cat_Det')
]