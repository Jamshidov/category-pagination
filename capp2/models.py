from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "1. Продукты"
