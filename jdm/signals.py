from datetime import datetime
from django.contrib.auth.models import User, Group
from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author


def request_start_handler(sender, **kwargs):
    print('Request started at', datetime.now())


@receiver(request_finished)
def request_finished_handler(sender, **kwargs):
    print('Request finished at', datetime.now())


@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
        group, c = Group.objects.get_or_create(name='casual_author')
        instance.groups.add(group)
    print('New author is created and added to group casual_author')


@receiver(post_save, sender=User)
def save_author(sender, instance, **kwargs):
    instance.author.save()
    print('Author is saved')