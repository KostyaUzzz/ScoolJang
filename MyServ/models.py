from django.db import models


class Product(models.Model):
    product_name = models.CharField(verbose_name='наименование товара', max_length=128, blank=False)
    description = models.TextField(verbose_name='описание', max_length=254, blank=True)
    photo = models.ImageField(upload_to='product_photo', blank=False, default='/unknowing/default.png')
    category = models.CharField(verbose_name='категория товара/ тип', max_length=64, blank=False)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.product_name