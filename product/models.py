from django.db import models

from provider.models import Providers

#2. Create a table called products, with the following properties: id, name, price, description, timestamps. You can add more properties if you want.
class Products(models.Model):
    name = models.CharField(max_length=75)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50)
    timestamps = models.DateTimeField(auto_now_add=True)
    #3. Add a relationship between products and providers.
    provider = models.ForeignKey(Providers, on_delete=models.PROTECT)

    def __str__(self):
        return self.name