from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Photo
from .forms import PhotoForm

def photos_list(request):
    photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'photos/photos_list.html', {'photos':photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'photo': photo})

def photo_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.published_date = timezone.now()
            photo.save()
            return redirect ('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photos/photo_edit.html', {'form': form})
