from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>/', views.blog_category, name='blog_category'),
    path('tag/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.search_posts, name='post_search'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
    # Если нужны статические файлы (не через collectstatic)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
