from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('',include('about.urls')),
    path('authentication/',include('authentication.urls')),
    path('',include('post.urls')),
    path('',include('auctionItem.urls')),
    path('auctionItem/',include('auctionItem.urls')),
    path('live/',include('live.urls'))
    

    
]
