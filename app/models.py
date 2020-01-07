from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=True, default='')
    description = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name