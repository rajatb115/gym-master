from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    about = models.TextField()
    contact_phone = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=100,default='none')

    def __str__(self):
        return '%s' % self.name