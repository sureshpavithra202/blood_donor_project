from django.db import models


class Donor(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name 