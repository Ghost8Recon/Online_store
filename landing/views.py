from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()

    return render (request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category_id=2)
    products_images_new = products_images.filter(product__category_id=1)
    return render (request, 'landing/home.html', locals())
