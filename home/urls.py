from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', views.my_admin, name='admin'),
]
