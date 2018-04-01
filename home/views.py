from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from products.models import ProductImage, ProductType, Companiya, Place
from django.contrib import admin


def home(request):
    products_images_list = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True).order_by(
        '-created')[0:50]
    productType = ProductType.objects.all()

    query = request.GET.get("q")
    if query:
        products_images_list = products_images_list.filter(product__name__icontains=query)



    paginator = Paginator(products_images_list, 10)  # Show 25 products per page

    page = request.GET.get('page')
    try:
        products_images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products_images = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products_images = paginator.page(paginator.num_pages)

    companiya = Companiya.objects.all()
    place = Place.objects.all()[0:1]

    products_images_t = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    context = {
        "products_images": products_images,
        "products_images_t": products_images_t,
        "companiyas": companiya,
        "places": place,
        "productType": productType,
    }
    return render(request, 'landing/home.html', context)


def my_admin(request):
    return render(request, admin)
