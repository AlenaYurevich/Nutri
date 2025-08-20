from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helen.urls')),  # Все URL приложения helen

]


handler404 = 'helen.views.handler404'
handler500 = 'helen.views.handler500'
