from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^movie_main', views.index,name="movie"),
    url(r'^login.html$',views.login),
    url(r'^register.html$', views.register),
    url(r'^prediction.html$', views.pred,name="pred"),
    url(r'^recommendation.html$', views.reco, name="reco"),



]
