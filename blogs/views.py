from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Blogs
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        page_obj = Blogs.objects.filter(title__icontains=q)
        data = {
            'page_obj': page_obj
        }

    else:

        blogs = Blogs.objects.all()
        paginator = Paginator(blogs, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'page_obj': page_obj
        }
    return render(request, "blogs/home.html", data)
