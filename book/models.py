from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

def minlength10_validator(value):
    if len(value) < 10:
        raise forms.ValidationError('10자리 이상만 입력 가능!!!!')

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    publisher = models.CharField(max_length=50, validators=[minlength10_validator])
    publication_date = models.DateField(auto_now_add=True)
    ip = models.CharField(max_length=15)
    photo = models.ImageField(blank=True)
    photo2 = models.ImageField(blank=True, upload_to='book')
    photo3 = models.ImageField(blank=True, upload_to='book/%Y/%m/%d')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:book_list')

from django import forms
class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publisher', 'photo', 'photo2', 'photo3']
        labels = {'title':'ModelForm_책제목', 'author':'ModelForm_저자', 'publisher':'ModelForm_출판사'}
        help_texts = {'author':'작가 이름을 3자리 이상으로 입력하세요',
                        'ip':'ip주소는 자동으로 들어갑니다.'}
