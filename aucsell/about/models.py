from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=200)



    def __str__(self):
        return self.name