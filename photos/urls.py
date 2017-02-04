from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photos_list, name='photos_list')
]
