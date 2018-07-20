from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView
from .models import blog_post
from django.shortcuts import render

def index(request):
    return render(request,'accounts.html')


class blog_view(ListView):
    model = blog_post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = blog_post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = blog_post
    template_name = 'post_new.html'
    fields ='__all__'

class BlogUpdateView(UpdateView):
    model = blog_post
    fields = ['title','post']
    template_name = 'post_edit.html'