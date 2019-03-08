from django.urls import path, re_path, register_converter
from django.conf.urls import url, re_path
from . import views
from .Myconverters import CodeConverter

app_name = "scoops"

register_converter(CodeConverter, "mycode")

urlpatterns = [
    path('', views.func1, name="index"),
    #url(r'^(?P<year>[0-9]{4})/$', views.func2, name="my2"),
    re_path(r'^(?P<year>[0-9]{4})/$', views.func2, name="my2"),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>\d{2})/$', views.func3, name="my3"),
    re_path(r'^(?P<aa>\w{4})/$', views.func4, name="my4"),
    re_path(r'^(?P<aa>\w{4})/(?P<bb>\w{2})/$', views.func5, name="my5"),
    path('article/<int:year>/<int:month>/<slug:myname>/', views.func6),
    path('article5/<mycode:num>/', views.func7)
]
