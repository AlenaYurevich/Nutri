from django.urls import path
from .views import idmt_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', idmt_view, name='calc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
