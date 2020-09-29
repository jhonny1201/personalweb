from django.shortcuts import render, get_object_or_404
from .models import Categories, Post


# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categories = Categories.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts, 'categories':categories})

def category(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'blog/category.html', {'category': category})

