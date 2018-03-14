from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^$', views.html, name='nourl'),
    url(r'^about$', views.html, name='nourl'),
    url(r'^contact$', views.html, name='nourl'),
]