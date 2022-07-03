from django.contrib import admin
from django.conf.urls import include, url
from contacts import views


urlpatterns = [
  url(r'^api/', views.contact_list),
]
