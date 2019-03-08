from django.contrib import admin
from .models import Reporter, Article, Publication,Restaurant, Waiter, Place

# Register your models here.

admin.site.register(Reporter)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Place)

