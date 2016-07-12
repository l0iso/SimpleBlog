from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    post_head = models.CharField("Head",max_length=150)
    post_text = models.CharField(max_length=10000)
    post_date = models.DateTimeField('date published')
    post_author = models.CharField(max_length=20)
    post_condition = models.BooleanField(default= False)

    def __str__(self):
        return self.post_head


class Comments(models.Model):
    comment_text = models.CharField(max_length=500)
    comment_author = models.CharField(max_length=20)
    comment_date = models.DateTimeField('comment date')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_text