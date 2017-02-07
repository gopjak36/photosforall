from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Photo

def photos_list(request):
    photos = Photo.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'photos/photos_list.html', {'photos':photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photos/photo_detail.html', {'photo': photo})
