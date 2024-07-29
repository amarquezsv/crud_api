from django.db import models

#1. Create a table called providers, with the following properties: id, name, address, phone, description, timestamps. You can add more properties if you want.
class Providers(models.Model):
    name = models.CharField(max_length=75)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    timestamps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
