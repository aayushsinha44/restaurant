from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(primary_key=True)
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15, null=True, blank=True)
    picture_url=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.email)

class Address(models.Model):
    email=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    pincode=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)



