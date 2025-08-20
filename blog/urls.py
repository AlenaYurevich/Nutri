from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<slug:category_slug>/', views.blog_category, name='blog_category'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
