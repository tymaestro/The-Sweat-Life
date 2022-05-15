from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    activity = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f"{self.content} by {self.name}"
