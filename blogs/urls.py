from django.urls import path

from . import views

urlpatterns = [
    # this code serves the http response from the views.py
    path("", views.index, name="index"),
    path('remove-blog/<slug:slug>/', views.remove_blog, name="remove-blog"),
    path('update-blog/<blog_id>/', views.update_blog, name="update-blog"),
    path('blog/<slug:slug>/', views.blog_detail, name="blog-detail"),
]
