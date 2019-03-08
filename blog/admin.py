from django.contrib import admin
from .models import Post, Musician, Album, FieldTest, Person,Comment,Profile


# Register your models here.
admin.site.register(Post)
admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(FieldTest)
admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Profile)
