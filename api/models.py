from django.db import models



class message(models.Model):
    name = models.TextField()
    email = models.EmailField(primary_key=True)
    message = models.TextField()
