from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField()
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title