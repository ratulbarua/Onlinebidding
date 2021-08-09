from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post/',views.post , name = 'post'),
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)