from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# from django.contrib.auth.models import AbstractUser
# from django.utils.timezone import now
# Create your models here.

# Create your models here.
ROLE_CHOICES = [
    ('Student', 'Student'),
    ('Trainer', 'Trainer'),
    ('Wellness Organization', 'Wellness Organization')
]

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title

    def str(self):
        return self.title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True, default="This is your bio.")
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Student')
    profile_image = models.ImageField(upload_to="profile_pics/", default="profile_pics/default.jpg")


    def __str__(self):
        return f"{self.user.username}'s Profile"
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Author(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

