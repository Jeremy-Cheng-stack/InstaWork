from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100, default='First Name')
    lname = models.CharField(max_length=100, default='Last Name')
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + ' ' + self.lname