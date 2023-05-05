from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime
# Create your models here.

class Product(models.Model):
    x=[
        ('laptop','laptop'),
        ('computer','computer'),
        ('phone','phone')
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    content = models.TextField()
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100,null=True, blank=True,choices=x)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Product_tb'
        #ordering = ['content']
        ordering = ['-price']

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null = True)
    created = models.DateTimeField(default=datetime.now)


class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Lg(models.Model):
    name = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Register(models.Model):
    name = models.CharField(max_length=150,unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)


