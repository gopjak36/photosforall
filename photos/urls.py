from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photos_list, name='photos_list'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.photo_detail, name='photo_detail'),
    url(r'^photo/new/$', views.photo_new, name='photo_new'),
]
