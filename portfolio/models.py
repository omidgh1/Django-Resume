from django.db import models


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')


class ContactInfo(models.Model):
    name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='personal/')

    def __str__(self):
        return self.email
