from django.db import models
from autoslug import AutoSlugField
class ContactApp(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

    # new_slug=AutoSlugField(populate_from='name',unique=True,null=False,default=None)
