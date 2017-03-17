from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^movie_main', views.index,name="movie"),
    url(r'^login.html$',views.login),
    url(r'^register.html$', views.register),
     

]
