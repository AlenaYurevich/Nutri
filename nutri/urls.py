from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helen.urls')),
    path('blog/', include('blog.urls')),  # Все URL приложения helen

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'helen.views.handler404'
handler500 = 'helen.views.handler500'
