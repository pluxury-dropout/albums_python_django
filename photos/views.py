from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AlbumForm, PhotoUploadForm
from .models import Album, Photo

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'photos/register.html', {'form': form})

def home(request):
    public_albums = Album.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'photos/home.html', {'albums': public_albums})

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()
            return redirect('profile')
    else:
        form = AlbumForm()
    return render(request, 'photos/album_form.html', {'form': form})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('album-detail', pk=photo.album.id)
    else:
        form = PhotoUploadForm(request.user)
    return render(request, 'photos/photo_upload.html', {'form': form})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    if not album.is_public and album.user != request.user:
        return redirect('login')
    return render(request, 'photos/album_detail.html', {'album': album})

@login_required
def profile(request):
    return render(request, 'photos/profile.html')