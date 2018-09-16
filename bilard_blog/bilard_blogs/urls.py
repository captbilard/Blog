from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('post/<int:post_id>/', views.post, name = 'post'),
    #path('homepage/', views.homepage, name = 'homepage'),
    
]

#"""+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)"""
