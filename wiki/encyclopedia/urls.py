from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.newpage, name="newpage"),
    path("edit/<str:entryName>", views.editpage, name="edit"),
    path('<str:entryName>', views.entry, name='entry'),
]
