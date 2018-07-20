from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'base.html'



#class BlogCreateView(CreateView):
  #  model = Post
 #   template_name = 'post_new.html'
 #   fields = '__all__'
