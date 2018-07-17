from django.db import models

class Category(models.Model):
    name = models.CharField('category title', max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Product(models.Model):
    name = models.CharField('product title', max_length=200)
    pub_date = models.DateField( 'date published')
    brand = models.CharField('product brand', max_length=200)
    price = models.IntegerField('product price', default=0)
    image =  models.CharField('image url', max_length=255, default='DEFAULT VALUE')
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
