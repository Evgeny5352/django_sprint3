from blog.models import Post, Category
import datetime as dt
from django.shortcuts import render, get_object_or_404

date_now = dt.datetime.now(tz=dt.timezone(dt.timedelta()))


def index(request):
    posts = Post.objects.filter(is_published=True,
                                pub_date__lte=date_now,
                                category__is_published=True
                                ).order_by('-pub_date')[:5]
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):

    post = get_object_or_404(Post, is_published=True,
                             category__is_published=True,
                             pub_date__lte=date_now,
                             id=id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug,
                                is_published=True,
                                pub_date__lte=date_now)
    category = get_object_or_404(Category,
                                 is_published=True,
                                 slug=category_slug)
    context = {'posts': posts,
               'category': category}
    return render(request, 'blog/category.html', context)
