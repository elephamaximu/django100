from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):

    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                    related_name='shop_post_set')
    title = models.CharField( verbose_name='shp앱..제목',  max_length=100)
    content = models.TextField()
    #admin UI가 없다.
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


STATUS_CHOICES = (
('d', 'Draft'),
('p', 'Published'),
('w', 'Withdrawn'),
)
class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id']

    def get_absolute_url2(self):
        print(self)
        return reverse("shop:detail", args=[self.id])

    def get_absolute_url(self):
        return reverse("shop:detail", kwargs={"pk": self.id})
        # return reverse("shop:list")
    

