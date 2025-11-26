from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    color = models.CharField(max_length=15)
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    is_new = models.BooleanField()


    def __str__(self):
        return self.name

# Create your models here.
