from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'shop'

urlpatterns = [
    path('', views.article_list, name='list' ),
    #path('<pk>/detail/', views.article_detail, name='detail'),
    path('<pk>/detail/', views.ArticleDV.as_view(), name='detail'),
    path('mine/', views.MyView.as_view()),
    path('home/', views.HomePageView.as_view()),
    path('go/', RedirectView.as_view(url="https://djangoproject.com")),
    path('go2/', RedirectView.as_view(url="/shop/home")),
    path('thanks/', views.success),
    path("contact/", views.ContactView.as_view()),
    
    path("new/", views.article_new, name="new"),
    path("<pk>/edit/", views.article_edit, name="edit"), #1/edit/
    path("<pk>/del/", views.article_del, name="del"),
    path('reversetest/', views.article_reversetest, name="rtest2"),
    path('temptest', views.template_test, name ='ttest'),
    path('insert/', views.article_insert, name='insert' ),
    path('delete/', views.article_delete, name='delete' ),
    path('update/', views.article_update, name='update' ),
    path('test1/', views.test1, name='rtest1'),
    path('test2/', views.test2),
    path('test3/', views.test3),
]

