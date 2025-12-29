from .models import Post, Tag, Category


def recent_posts(request):
    recent = Post.objects.all().order_by('-created_on')[:4]  # 4 последних поста
    return {'recent_posts': recent}


def all_tags(request):
    return {
        'all_tags': Tag.objects.all().order_by('name')
    }


def all_categories(request):
    return {
        'all_categories': Category.objects.all().order_by('name')
    }
