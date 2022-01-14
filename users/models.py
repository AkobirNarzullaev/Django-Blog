from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #CASCADE -> if user is deleted then delete the profile as well but not vice versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)    #self.image.path will open the image of the current instance

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)