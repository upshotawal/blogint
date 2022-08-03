from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Blogs
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import BlogForm

# Create your views here.


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        page_obj = Blogs.objects.filter(title__icontains=q)[:16]
        data = {
            'page_obj': page_obj
        }

    else:

        blogs = Blogs.objects.order_by('?')
        paginator = Paginator(blogs, 16)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {
            'page_obj': page_obj
        }
    return render(request, "blogs/home.html", data)


def remove_blog(request, slug):
    if request.method == 'GET':
        c = get_object_or_404(Blogs, slug=slug)
        c.delete()
        messages.success(request, "Blog has been Deleted")
    return redirect("index")


def blog_detail(request, slug):
    post = get_object_or_404(Blogs, slug=slug)
    related_blog = Blogs.objects.exclude(title=post.title)[:10]

    return render(request, 'blogs/blofvew.html', {'post': post, 'related_blog': related_blog})


def update_blog(request, blog_id):
    blogs = Blogs.objects.get(pk=blog_id)
    form = BlogForm(request.POST or None, instance=blogs)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'blogs/update.html', {'form': form, 'blogs': blogs})
