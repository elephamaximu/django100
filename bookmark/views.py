from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark  #object_list를 가지고 bookmark_list.html로 render 

class BookmarkDV(DetailView):
    model = Bookmark  #object를 가지고 bookmark_detail.html로 render 



