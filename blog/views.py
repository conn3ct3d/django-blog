from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)