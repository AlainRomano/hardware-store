from django.db import models

city_choices = (
    ('pt', 'Potosi'),
    ('sc', 'Santa Cruz'),
    ('cbba', 'Cochabamba'),
)
class Provider(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=10, choices=city_choices, default='pt')
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to='provider/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")
        ordering = ['id']
    

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)

    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")
        ordering = ['id']



gender_choices = (
    ('male', 'Male'),
    ('female', 'Female'),
)
class Client(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    dni = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=gender_choices, default='male')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")
        ordering= ['id']


