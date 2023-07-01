from django.utils import timezone

from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post

DATE_NOW = timezone.now()
POSTS_PAGE = 5


def index(request):
    posts = Post.objects.filter(is_published=True,
                                pub_date__lte=DATE_NOW,
                                category__is_published=True
                                )[:POSTS_PAGE]
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):

    post = get_object_or_404(Post, is_published=True,
                             category__is_published=True,
                             pub_date__lte=DATE_NOW,
                             id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(Category.objects.filter(
        is_published=True), slug=category_slug)
    posts = category.posts_category.filter(is_published=True,
                                           pub_date__lte=DATE_NOW)
    context = {'posts': posts,
               'category': category}
    return render(request, 'blog/category.html', context)
