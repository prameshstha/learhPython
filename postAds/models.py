import os
from django.db import models
from django.conf import settings


# Create your models here.
from django.utils.safestring import mark_safe
from markdown import markdown


def get_image_path(instance, filename):
    return os.path.join('images', str(instance.id), filename)


class PostAd(models.Model):
    # post_user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_body = models.CharField(max_length=250)
    post_image = models.ImageField(upload_to='images/',
                                   null=True,
                                   blank=True,)
    post_category = models.CharField(max_length=50)
    post_created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.post_title


