from django.db import models
from django.db.models import permalink

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_product_category', None, { 'slug': self.slug })

class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    addded = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('products.Category')
    image = models.FileField(upload_to='product')
    price = models.DecimalField(max_digits=8, decimal_places=2,default='0.0')

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_product', None, { 'slug': self.slug })