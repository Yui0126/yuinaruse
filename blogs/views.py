from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

from .models import Post, Comment

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    # template = 'blogs/index.html'
    # template = loader.get_template("blogs/index.html")
    # return HttpResponse(template.render({'posts': posts}, request))
    # return render(request, template, {'posts': posts})
    return render(request, "blogs/index.html", {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post).order_by("-created_at")
    return render(request, "blogs/detail.html", {'post': post, 'comments': comments})

def comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        if author and text:
            Comment.objects.create(post=post, author=author, text=text)
    return redirect("blogs:detail", post_id=post.id)

def about(request):
    return render(request, 'blogs/about.html')