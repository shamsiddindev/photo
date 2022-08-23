from django.shortcuts import render
from django.views.generic import ListView
from .models import PostModel


class PostListView(ListView):
    queryset = PostModel.objects.order_by('-id')
    template_name = 'gallery.html'
