from django.shortcuts import render, redirect, reverse
from django import forms
from .models import Book

def minlingth3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상입니다.....")

class BookForm(forms.Form):
    title = forms.CharField(label="forms 제목")
    author = forms.CharField(label="forms 저자", validators=[minlingth3_validator])
    publisher = forms.CharField(label="forms 출판사", required=False)
    
    def save2(self, commit=True):
        book = Book(**self.cleaned_data) 
        if commit:
            book.save()
        return book
    
