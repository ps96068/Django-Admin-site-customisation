from django.db import models

class Shop(models.Model):

    class Meta:
        db_table = 'shop'

    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Image(models.Model):

    class Meta:
        db_table = 'image'

    title = models.CharField(max_length=255)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Product(models.Model):

    class Meta:
        db_table = 'product'

    title = models.CharField(max_length=255)
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
