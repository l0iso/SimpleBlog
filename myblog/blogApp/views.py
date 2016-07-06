from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

from .models import BlogPost, Comments


def index(request):
    '''Show All posts'''
    posts_list = BlogPost.objects.all().order_by('-post_date')
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(posts=posts)
    return render_to_response('blogApp/index.html', vars, context_instance=RequestContext(request))

def detail (request, post_id):
    try:
        this_post = BlogPost.objects.get(pk=post_id)
    except BlogPost.DoesNotExists:
        raise Http404('Post does not exist')

    this_comments = Comments.objects.filter(post=this_post)

    return render(request, 'blogApp/detail.html', {'this_post': this_post, 'this_comments': this_comments})