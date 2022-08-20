from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class VirtualUser(models.Model):
    STATUS = [
        ('Single', 'Single'),
        ('In relationship', 'In relationship'),
        ('Married', 'Married'),
        ('Hidden', 'Hidden')
    ]

    first_name = models.CharField(max_length=25, null=True, blank=True)
    middle_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    nickname = models.CharField(max_length=25, unique=True)
    age = models.IntegerField(null=True, blank=True)
    photoImage = CloudinaryField('image')
    status = models.CharField(max_length=35, choices=STATUS)
    phone = models.CharField(max_length=35,null=True, blank=True)
    description = models.TextField(max_length=500)
    virtual_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
