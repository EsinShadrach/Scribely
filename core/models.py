from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(
        unique=True
    )
    avatar = models.ImageField(
        null=True,
        default='profile_img.jpg'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return self.username



class Note(models.Model):
    name = models.CharField(max_length=255)
    tag1 = models.SlugField(max_length=20, blank=True, null=True)
    tag2 = models.SlugField(max_length=20, blank=True, null=True)
    tag3 = models.SlugField(max_length=20, blank=True, null=True)
    note = models.TextField(blank=False)
    unique_note_identity = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4()
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
