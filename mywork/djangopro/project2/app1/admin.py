from django.contrib import admin

from .models import blog_post,comment

admin.site.register(blog_post)
admin.site.register(comment)
