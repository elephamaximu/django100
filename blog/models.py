from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
#class1개가 테이블1개 
class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                    related_name='blog_post_set', blank=True)
    title = models.CharField( verbose_name='제목',  max_length=100)
    content = models.TextField()
    #admin UI가 없다.
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def latlng_validation(value):
        check = re.match(r'(\d+\.?\d*),(\d+\.?\d*)', value)
        if not check:
            raise ValidationError("유효하지않은 위도, 경도입니다.")
    latlng = models.CharField(max_length=100, blank=True,
                validators=[latlng_validation],
                help_text="위도와 경도를 입력하세요")


    def validation_even(value):
        if value%2!=0:
            raise ValidationError(str(value) + "가 짝수이어야합니다.")

    even_field = models.IntegerField(validators=[validation_even])
    str_field = models.CharField(max_length=50)
    str_field2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title + " ---  id는"  + str(self.id)
    class Meta:
        ordering=['title', '-id']  #id로 ascening 


class Musician(models.Model):
    first_name = models.CharField(max_length=50)        
    last_name = models.CharField(max_length=50)        
    instrument = models.CharField(max_length=50)  

    def __str__(self):
        return self.first_name + self.last_name     

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.name

import datetime

#from jsonfield import JSONField  #JSONField()
#import jsonfield #jsonfield.JSONField()
#from django.contrib.postgres.fields import JSONField
import json

class Person(models.Model):
    name = models.CharField(max_length=255)#null=False  blank=False
    bio = models.CharField(max_length=500, blank=True) #null=False ===> (빈문자 : '')
    bio2 = models.CharField(max_length=500, null=True) #null=True, blank=False ...논리에러 (필수칼럼이다)
    bio3 = models.CharField(max_length=500, null=True,blank=True)  #==> Null
    birth_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    def contact_default():
        data = {"email":"zzilre@daum.net"}
        return json.dumps(data)

    contact_info = models.TextField("연락처", default = contact_default)
    
    
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR='JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICE=(
      (FRESHMAN, '1학년'),
      (SOPHOMORE, '2학년'),
      (JUNIOR, '3학년'),
      (SENIOR, '4학년'),
      )
    year_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICE,
                  default = FRESHMAN)

    


class FieldTest(models.Model):
    fAutoField = models.AutoField(primary_key=True)
    fBigIntegerField = models.BigIntegerField(default=1)
    fBooleanField = models.BooleanField(default=True)
    fCharField = models.CharField(default='엔코아', max_length=30)
    
    #auto_now :  현재일자로 저장시마다 수정?False이므로 수정불가 
    fDateField = models.DateField(auto_now=False, default=datetime.date.today)
    
    #auto_now = True:  현재일자, 저장시마다 수정불가 
    #auto_now = False:  현재일자, 저장시마다 수정된다.  
    #auto_now_add =true:현재일자로 1회만 들어간다. 
    #auto_now_add =false:선택일자로 1회만 들어간다. 
    
    fDateTimeField = models.DateTimeField(auto_now=False, auto_now_add=False)

    fDecimalField = models.DecimalField(default=1.7321, decimal_places=4, max_digits=10)
    fEmailField = models.EmailField(default="email@example.com")
    fFloatField = models.FloatField(default=1.7321)
    fIntegerField = models.IntegerField(default=10)
    fGenericIPAddressField = models.GenericIPAddressField(protocol='both', unpack_ipv4=True, default=None)
    fNullBooleanField = models.NullBooleanField(default=True)
    fPositiveIntegerField = models.PositiveIntegerField(default=100)
    fPositiveSmallIntegerField = models.PositiveSmallIntegerField(default=50)
    fSlugField = models.SlugField(max_length=30, default='slug')
    fSmallIntegerField = models.SmallIntegerField(default=-50)
    fTextField = models.TextField(default="text text text text text text text")
    fURLField = models.URLField(max_length=200, default='http://localhost')        



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

