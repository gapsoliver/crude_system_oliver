from django.db import models

class People(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    age = models.IntegerField(max_length=30, blank=False, null=False)
    gender = models.CharField(max_length=30, blank=False, null=False)
    phonenumber= models.IntegerField(max_length=30, blank=False, null=False)
    amount = models.IntegerField(max_length=30, blank=False, null=False)


def __self__(self):
    return self.name