from django.conf.urls import url
from products import views

urlpatterns = [
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    url(r'^product/addcomment/(?P<id>\w+)/$', views.addcomment, name='addcomment'),
    url(r'^cat/(?P<category_name>\w+)', views.category, name='category'),
    url(r'^cat/', views.all, name='all'),
]