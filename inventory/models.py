from django.db import models

# Create your models here.


class Item(models.Model):
    Item_name = models.CharField(max_length=200)
    Item_quantity = models.IntegerField()

    def __str__(self):
        return self.Item_name

    def is_empty(self):
        return self.Item_quantity <= 0
    





