from django.db import models

# Create your models here.


class Blogs(models.Model):
    # define different fields/columns for package
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    decription = models.CharField(max_length=550)
    readtiem = models.CharField(max_length=50)
    authname = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
