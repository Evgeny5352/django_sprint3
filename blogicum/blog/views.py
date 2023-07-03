from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from blog.models import Category, Post
from .const import POSTS_PAGE


def index(request):
    posts = Post.objects.filter(is_published=True,
                                pub_date__lte=timezone.now(),
                                category__is_published=True
                                )[:POSTS_PAGE]
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):

    post = get_object_or_404(Post, is_published=True,
                             category__is_published=True,
                             pub_date__lte=timezone.now(),
                             id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(
        is_published=True), slug=category_slug)
    posts = category.posts.filter(is_published=True,
                                  pub_date__lte=timezone.now())
    context = {'posts': posts,
               'category': category}
    return render(request, 'blog/category.html', context)
