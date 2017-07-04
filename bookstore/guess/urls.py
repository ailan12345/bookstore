from django.conf.urls import url
from guess import views


urlpatterns = [
    url(r'^$', views.guess, name='guess'),
    url(r'^game/$', views.game, name='game'),
   
]