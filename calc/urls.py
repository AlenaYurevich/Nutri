from django.urls import path
from .views import calculation_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', calculation_view, name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
