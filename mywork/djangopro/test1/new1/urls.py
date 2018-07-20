from django.conf.urls import url
from new1 import views

urlpatterns = [
    url(r'^$', views. BlogListView.as_view()),
    #url(r'^post_new/$', views.BlogDetailView.as_view()),
     #url(r'^base/$', views. BlogCreateView.as_view()),
]
