from django.db import models


class Post(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to ='images/')
    description = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title