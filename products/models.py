from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


# Create your models here.
class ProductType(models.Model):
    class Meta:
        verbose_name_plural = 'тип'
        verbose_name = 'типы'

    image = models.ImageField(upload_to='products_type_images/')
    name = models.CharField(max_length=20, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name


class Product(models.Model):
    class Meta:
        verbose_name_plural = 'запчасть'
        verbose_name = 'запчасти'

    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.TextField(blank=True, null=True, default=None, max_length=100)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    type = models.ForeignKey(ProductType, blank=True, null=True, default=None)

    def __str__(self):
        return "(%s, %s)" % (self.id, self.name)


class ProductImage(models.Model):
    class Meta:
        verbose_name_plural = 'фотография_запчасти'
        verbose_name = 'фотографии_запчасти'

    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)


class Companiya(models.Model):
    class Meta:
        verbose_name_plural = 'Компания'
        verbose_name = 'Компания'

    Tel_Nomer = models.CharField(max_length=20, blank=True)
    Whatsapp_Nomer = models.CharField(max_length=20, blank=True)
    Email = models.EmailField(blank=True)

    def __str__(self):
        return "(%s, %s, %s)" % (self.Tel_Nomer, self.Email, self.Whatsapp_Nomer)


class Comment(models.Model):
    class Meta:
        verbose_name_plural = 'Комментария'
        verbose_name = 'Комментарии'

    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product)
    comment = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "на %s,  %s написал %s" % (self.product.name, self.name, self.comment)

class Place(models.Model):
    class Meta:
        verbose_name_plural = 'Место на карте'
        verbose_name = 'Место на карте'

    url = models.TextField()

    def __str__(self):
        return "%s" % self.url
