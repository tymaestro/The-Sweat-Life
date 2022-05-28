""" Modules """
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Activity(models.Model):
    """ Fields for Activity model creation  """
    title = models.CharField(max_length=100, unique=True)
    athlete = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="activities"
        )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Orders activities by most recent published date """
        ordering = ['-pub_date']

    def __str__(self):
        """ Returns title string """
        return self.title

    def get_absolute_url(self):
        """ Redirects user to activities page """
        return reverse('activities')


class Comment(models.Model):
    """ Fields for Comment model creation  """
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="comments"
        )
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Orders comments by most recent published date """
        ordering = ['-pub_date']

    def __str__(self):
        """ Returns content string """
        return self.content
