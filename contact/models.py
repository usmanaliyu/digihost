from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField(max_length=2000, blank=False)


    def __str__(self):
        return self.name
