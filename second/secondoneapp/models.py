from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class secondoneappModules(models.Model):
    title=models.CharField(max_length=20)
    sec_desc=HTMLField()

# x_slug=AutoSlugField(populate_from='title',unique=True,null=False,default=None)
# Create your models here.
