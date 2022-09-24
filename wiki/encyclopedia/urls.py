from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.newpage, name="newpage"),
    path('<str:entryName>', views.entry, name='entry'),
]
