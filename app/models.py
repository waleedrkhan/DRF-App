from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=True, default='')
    description = models.TextField()
    price = models.IntegerField(blank=True, default=10)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    items = models.ManyToManyField(Product)


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.PROTECT)
    items = models.ManyToManyField(Product)
    user = models.ForeignKey('auth.User', related_name="orders", on_delete=models.PROTECT)
