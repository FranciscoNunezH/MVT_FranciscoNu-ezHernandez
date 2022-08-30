from mailbox import NoSuchMailboxError
from django.db import models


# Create your models here.
class familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=0)
    nacimiento = models.DateField("Birth Name")

