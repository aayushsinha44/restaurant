from django.db import models
from user.models import User, Address
from datetime import datetime

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    small_description=models.CharField(max_length=255)
    description=models.TextField()
    icon_image=models.ImageField()
    rating=models.FloatField()

    def __str__(self):
        return self.name

class ItemImage(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    image=models.ImageField()

    def __str__(self):
        return str(self.id)

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class ItemCategory(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=255)

    def __str__(self):
        return self.subcategory_name

class ItemSubCategory(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class PriceCurrency(models.Model):
    currency=models.CharField(max_length=255)
    is_active=models.BooleanField()

    def __str__(self):
        return self.currency

class OrderStatus(models.Model):
    order_status=models.CharField(max_length=25)

    def __str__(self):
        return self.order_status

class Order(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Review(models.Model):
    email=models.ForeignKey(User, on_delete=models.CASCADE)
    review=models.TextField()
    date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)

class ReviewItem(models.Model):
    email=models.ForeignKey(User, on_delete=models.CASCADE)
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    review=models.TextField()
    date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)


