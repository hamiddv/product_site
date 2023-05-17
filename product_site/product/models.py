from django.db import models

import datetime


class Category(models.Model):
    category = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Brand(models.Model):
    brand = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Product(models.Model):
    name = models.CharField(
        max_length=256
    )

    price = models.FloatField()
    description = models.CharField(
        max_length=2024
    )

    available = models.BooleanField(
        default=False
    )

    image = models.ImageField(
        upload_to="./media/product/img/%y/%m/%d/"
    )

    # color = models.JSONField(
    #     null=True,
    #     blank=True
    # )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True, blank=True
    )

    # def __str__(self):
    #     self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


