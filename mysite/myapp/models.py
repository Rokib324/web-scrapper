from django.db import models

class Link(models.Model):

    def __str__(self):
        return self.name or 'No Name'

    address = models.CharField(max_length=1000, null=True, blank=True, default='')
    name = models.CharField(max_length=1000, null=True, blank=True, default='')

    
