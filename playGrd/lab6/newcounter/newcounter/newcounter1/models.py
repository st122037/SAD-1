from django.db import models

# Create your models here.
class Counter(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}, Value: {self.value}"