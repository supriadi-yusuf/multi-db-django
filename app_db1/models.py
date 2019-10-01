from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Member(models.Model):
    group = models.ForeignKey( Group, on_delete=models.CASCADE, \
            related_name="kelompok_group")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
