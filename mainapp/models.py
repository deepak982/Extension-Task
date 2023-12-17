from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.DecimalField(max_digits = 10,  decimal_places = 2 )
    category = models.CharField(max_length = 100)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    email_token = models.CharField(max_length=200)
    is_verify = models.BooleanField(default=False)


class data(models.Model):
    end_year = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=255)
    start_year = models.IntegerField(null=True, blank=True)
    impact = models.IntegerField(null=True, blank=True)
    added = models.DateTimeField()
    published = models.DateTimeField()
    country = models.CharField(max_length=255, blank=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.TextField()
    likelihood = models.IntegerField()