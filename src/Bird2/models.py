#  models.py
#  by: Islam Diaa
#      04 Oct 2017
#
from django.db import models


# Create your models here.
class Timeline(models.Model):
    content = models.CharField(max_length=250)
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    # user = should connect user !
