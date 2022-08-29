from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    title = models.CharField("TITLE", max_length=90, blank=False)
    description = models.TextField("DESCRIPTION", blank=True)
    url = models.URLField("URL", unique=True)

    def __str__(self):
        return self.title
