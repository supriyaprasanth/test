from django.conf.urls import url
from new import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views. AboutPageView.as_view()),
     url(r'^contact/$', views.ContactPageView.as_view()),
]
