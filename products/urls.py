from django.conf.urls import url
from products import views


urlpatterns = [
    #url(r'^landing/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]