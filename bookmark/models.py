from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField("url", unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
