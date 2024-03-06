from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
class Bid(models.Model):
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=13)
    description = models.TextField(max_length=1000)
    date = models.DateField('bid date')

    # Changing this instance method
    # does not impact the database, therefore
    # no makemigrations is necessary
    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'bid_id': self.id})
