from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Creator(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(default='default.jpg', upload_to='author_pics', null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(default='default.jpg', upload_to = 'post_pics')
    title = models.CharField(max_length = 100)
    content = models.TextField(default=None)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE, related_name='post')
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title