from django.db import models

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(blank=True, null=True, default=0, choices=[(i, i) for i in range(0, 101)], unique=False)

    def __str__(self):
        return self.name