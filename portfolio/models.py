from django.db import models


class ContactInfo(models.Model):
    name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='personal/')

    def __str__(self):
        return self.name
