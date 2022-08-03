from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Blogs

# Createavenue form


class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ('title', 'decription', 'readtiem',
                  'authname', 'designation', 'image')
