from __future__ import absolute_import, unicode_literals

import datetime

from django.utils import timezone

from celery import shared_task

from .models import Post


@shared_task(name="delete_posts")
def delete_post():
    posts = Post.objects.filter(
        is_published=False, created_at__lt=timezone.now() - datetime.timedelta(days=3)
    )

    posts.delete()
