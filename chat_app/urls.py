from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'chat_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('chat/', views.chat, name='chat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 