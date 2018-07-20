from django.db import models
from django.urls import reverse

# Create your models here.
class blog_post(models.Model):
    title  = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    post= models.TextField()

    def get_absolute_url(self):
       return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        """A string representation of the model."""
        return self.title

class comment(models.Model):
    post = models.ForeignKey(blog_post, on_delete=models.CASCADE)
    comm = models.CharField(max_length=140)

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.comment
