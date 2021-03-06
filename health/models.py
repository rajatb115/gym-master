from django.db import models
from django.db.models import permalink

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return ('view_health_category', None, { 'slug': self.slug })

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('health.Category')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_health_post', None, { 'slug': self.slug })
