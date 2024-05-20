from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from apps.shared.models import AbstractBaseModel


class Category(models.Model):
    cover = models.ImageField(upload_to="categories")
    name = models.CharField(max_length=100)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Product(models.Model):
    COLOR_CHOICE = [
        ("wh", "White"),
        ("bl", "Black"),
        ("br", "Brown"),
        ("g", "Green"),
        ("r", "Red"),
        ("y", "Yellow"),
        ("p", "Purple")
        ,
        ("k", "Khaki"),
        ("gr", "Gray"),
        ("or", "Orange")
    ]

    SIZE_CHOICE = [
        ("m", "M"),
        ("l", "L"),
        ("xl", "XL"),
        ("xxl", "XXL"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    seller = models.ForeignKey('users.User', on_delete=models.CASCADE)
    available_color = models.CharField(max_length=2, choices=COLOR_CHOICE, null=True)
    brand = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=3, choices=SIZE_CHOICE, null=True)
    count = models.IntegerField(default=0, null=True)
    is_active = models.BooleanField(default=True)
    like_count = models.IntegerField(default=0)
    objects = models.Manager()

    @property
    def imageURL(self):
        if self.cover:
            return self.cover.url
        else:
            return 'images/placeholder.png'

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    like_count = models.IntegerField(default=0)


class Favorite(models.Model):
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='favorites')
