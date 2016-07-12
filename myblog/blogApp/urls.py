from django.conf.urls import patterns, url
from . import  views
app_name = 'blog'
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^add_post/$', views.add_post, name= 'add_post'),
    url(r'^successful/$',views.success, name = 'successful')

]