from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Book
# Create your views here.

book_list = ListView.as_view(model=Book, paginate_by=10)
book_detail = DetailView.as_view(model=Book)
book_new = CreateView.as_view(model=Book, fields='__all__')
book_edit = UpdateView.as_view(model=Book, fields='__all__')
book_delete = DeleteView.as_view(model=Book, success_url='/book/')