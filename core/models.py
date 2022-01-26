from django.db import models

# Create your models here.


class Project(models.Model):
    """
    
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumnail = models.ImageField(upload_to='media/thumnails/', blank=True)
    kgPerDollar = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return self.name