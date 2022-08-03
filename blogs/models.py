from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Blogs(models.Model):
    # define different fields/columns for package
    title = models.CharField(max_length=250, unique=False)
    slug = AutoSlugField(populate_from='title', unique=True,
                         verbose_name="blog Slug")
    decription = models.CharField(max_length=550, unique=False)
    readtiem = models.CharField(max_length=50, unique=False)
    authname = models.CharField(max_length=100, unique=False)
    designation = models.CharField(max_length=50, unique=False)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
