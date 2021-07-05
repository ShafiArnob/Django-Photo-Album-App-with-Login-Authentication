from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.view_photo, name='photo'),
    path('add/',views.add_photo, name='add'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
