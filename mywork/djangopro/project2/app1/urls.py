from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='accounts'),
    path('home/', views.blog_view.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),


]