from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag
from django.core.paginator import Paginator
from helen.views import handle_forms
from django.db.models import Q


def blog_index(request):
    posts = Post.objects.all().order_by('order')
    paginator = Paginator(posts, 7)  # Show 7 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    forms_context = handle_forms(request)
    context = {
        "page_obj": page_obj,
        "breadcrumb_title": "База знаний",
        **forms_context,
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    forms_context = handle_forms(request)
    context = {
        "post": post,
        'breadcrumb_title': post.title,
        'breadcrumb_parent': 'База знаний',
        'breadcrumb_parent_url': '/blog',
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
        'posts': posts,  # здесь выводим посты Posts,
        'breadcrumb_parent': 'База знаний',
        'breadcrumb_parent_url': '/blog',
        ** forms_context,
    }
    return render(request, 'blog_category.html', context)


def search_posts(request):
    query = request.GET.get('q', '').strip()

    if query:
        # Ищем двумя способами и объединяем результаты
        query_lower = query.lower()

        # Поиск 1: стандартный icontains
        posts1 = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

        # Поиск 2: с приведенным к нижнему регистру запросом
        posts2 = Post.objects.filter(
            Q(title__icontains=query_lower) |
            Q(content__icontains=query_lower) |
            Q(description__icontains=query_lower) |
            Q(tags__name__icontains=query_lower)
        ).distinct()

        # Объединяем оба набора результатов
        posts = (posts1 | posts2).distinct().order_by('-created_on')
    else:
        posts = Post.objects.all().order_by('-created_on')

    # Пагинация
    paginator = Paginator(posts, 10)  # 10 постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_results.html', {
        'page_obj': page_obj,
        'query': query,
        'results_count': posts.count(),
        'breadcrumb_parent': 'База знаний',
        'breadcrumb_parent_url': '/blog',
    })


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags=tag).order_by('-created_on')
    forms_context = handle_forms(request)
    context = {
        'tag': tag,
        'posts': posts,
        'breadcrumb_title': f'Тег: {tag.name}',
        'breadcrumb_parent': 'База знаний',
        'breadcrumb_parent_url': '/blog',
        **forms_context,
    }
    return render(request, 'blog_tag.html', context)
