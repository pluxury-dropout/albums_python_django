from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from photos import views
from django.contrib.auth import views as auth_views  # Добавьте этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='photos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='photos/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('albums/new/', views.create_album, name='create-album'),
    path('albums/<int:pk>/', views.album_detail, name='album-detail'),
    path('photos/upload/', views.upload_photo, name='upload-photo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)