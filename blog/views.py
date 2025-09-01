from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator
from helen.views import handle_forms


def blog_index(request):
    posts = Post.objects.all().order_by('order')
    paginator = Paginator(posts, 7)  # Show 7 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    forms_context = handle_forms(request)
    context = {
        "page_obj": page_obj,
        **forms_context,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    forms_context = handle_forms(request)
    context = {
        "post": post,
        **forms_context,
    }
    return render(request, 'blog_detail.html', context)


def blog_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(
        categories__slug__contains=category_slug
    ).order_by(
        '-created_on')
    forms_context = handle_forms(request)
    context = {
        'category': category,
        'posts': posts  # здесь выводим посты Posts,
        ** forms_context,
    }
    return render(request, 'blog_category.html', context)
