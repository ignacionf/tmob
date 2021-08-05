import uuid
import json

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from django.forms.models import model_to_dict


class RedirectManager(models.Manager):

    def get_redirect(self, key):
        try:
            return json.loads(cache.get(key))
        except TypeError:
            raise Redirect.DoesNotExist(
                f"No existe Redirect con key = '{key}'")


class Redirect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=200, unique=True)
    url = models.URLField()
    active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = RedirectManager()

    def __str__(self):
        return self.key


@receiver(post_save, sender=Redirect)
def redirect_to_cache(sender, instance, **kwargs):

    if instance.active == True:
        data = model_to_dict(instance)

        # by : https://github.com/django/django/commit/89955cc35f3636684ea6f2a6c9504b35a3050f0f#diff-7c2adfa785135b665d47ca5f8a69dd4fe11ba34fe12a7b01be1e67559ab71599R55
        cache.set(instance.key, json.dumps(data), 2592000)


@receiver(post_delete, sender=Redirect)
def redirect_remove_cache(sender, instance, **kwargs):
    cache.delete(instance.key)
