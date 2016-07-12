from django.http import Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import  CommentsForm,PostForm
import  datetime
from django.shortcuts import redirect
# Create your views here.

from .models import BlogPost, Comments


def index(request):
    '''Show posts'''
    posts_list = BlogPost.objects.filter(post_condition = True).order_by('-post_date')
    paginator = Paginator(posts_list, 4)
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
        this_post = BlogPost.objects.get(pk=post_id,post_condition = True)
    except BlogPost.DoesNotExists:
        raise Http404('Post does not exist')
    this_comments = Comments.objects.filter(post=this_post)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_commint = form.save(commit= False)
            new_commint.comment_date = datetime.datetime.now()
            new_commint.save()
            return redirect("blog:detail", post_id)
    else:
        form = CommentsForm()
    return render(request, 'blogApp/detail.html', {'this_post': this_post, 'this_comments': this_comments,'form': form})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit = False)
            new_post.post_date = datetime.datetime.now()
            new_post.save()
            return  redirect("blog:successful" )
    else:
        form = PostForm()
    return render(request, 'blogApp/add_post.html',{'form':form})


def success(request):
    return render(request,'blogApp/successful.html')
