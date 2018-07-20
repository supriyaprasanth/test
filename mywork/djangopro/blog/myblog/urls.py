from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view())
]

