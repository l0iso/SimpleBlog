# coding: utf-8
from rest_framework import serializers
from .models import BlogPost, Comments


class PostSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ( 'post_head','post_text','id','post_author','post_condition')


class CommentsSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment_text','comment_author','id','post')