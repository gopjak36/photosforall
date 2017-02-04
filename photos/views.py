from django.shortcuts import render

def photos_list(request):
    return render(request, 'photos/photos_list.html', {})
