from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Album, Photo

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'is_public']

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['album', 'image', 'title']
    
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user is not None:
         self.fields['album'].queryset = Album.objects.filter(user=user)