from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><body bgcolor='yellow'><center><h1>HELLO THIS IS HOME PAGE OF THE BLOG</h1>Hello Anne<br><a href='h.html'>About</a><br><a href="">Contact</a></center></body></html>")
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
