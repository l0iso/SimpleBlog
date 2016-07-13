# coding: utf-8
from django.contrib import admin

from .models import BlogPost
from .models import Comments

admin.site.register(BlogPost)
admin.site.register(Comments)