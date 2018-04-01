from products.models import Product, Comment, Companiya, ProductImage, Place
from products.forms import CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def product(request, product_id):
    form = CommentForm
    comment = Comment.objects.filter(product=product_id).order_by('-created')
    product = get_object_or_404(Product, id=product_id)
    companiya = Companiya.objects.all()
    place = Place.objects.all()[0:1]

    content = {
        "companiyas": companiya,
        "places": place,
        "product": product,
        "form": form,
        "comment": comment
    }
    return render(request, 'products/product.html', content)


def addcomment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.product = Product.objects.get(id=id)
            form.save()
    return HttpResponseRedirect('/product/%s' % id)


def category(request, category_name):
    products_images_list = ProductImage.objects.filter(product__type__name__contains=category_name)
    companiya = Companiya.objects.all()
    place = Place.objects.all()[0:1]

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

    context = {
        "products_images": products_images,
        "companiyas": companiya,
        "places": place,
    }
    return render(request, 'landing/product.html', context)


def all(request):
    p = ProductImage.objects.all()
    companiya = Companiya.objects.all()
    place = Place.objects.all()[0:1]
    query = request.GET.get("q")
    if query:
        fp = p.filter(product__name__icontains=query)
        return render(request, 'landing/product.html',
                      {'products_images': fp, 'companiyas': companiya, 'places': place})
