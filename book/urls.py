from django.urls import path, re_path
from django.conf.urls import url

from . import views

app_name = "book"

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<pk>/detail/', views.book_detail, name='detail'),
    path("new/", views.book_new, name="new"),
    path("<pk>/edit/", views.book_edit, name="edit"),
    path("<pk>/delete/", views.book_delete, name="delete"),
    path("searchData/", views.searchData, name='search'),
]
