from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cart_adding/$', views.cart_adding, name='cart_adding'),
    url(r'^checkout/$', views.checkout, name='checkout'),
]
