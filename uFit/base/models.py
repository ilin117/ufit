from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ##topic = modles.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    description = models.TextField(null = True, blank = True)
    
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)


    class Meta:
        ordering = ['-update', '-created']

    def str(self):
        return self.title