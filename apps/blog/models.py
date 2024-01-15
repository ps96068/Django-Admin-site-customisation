from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Category(models.Model):

    class Meta:
        db_table = 'category'

    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def str(self):
        return self.name



class Post(models.Model):

    class Meta:
        db_table = 'post'

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def str(self):
        return self.title
