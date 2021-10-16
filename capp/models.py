from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    objects = models.Manager()

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = '1. Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('capp:category_link', kwargs={'slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", null=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    text = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/img/')
    price = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ('name', )
        verbose_name = 'Продукта'
        verbose_name_plural = '2. Продукты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('capp:product_detail', kwargs={'id': self.id, 'slug': self.slug})