# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class BookmarkLV(ListView):
    model = models.Bookmark


class BookmarkDV(DetailView):
    model = models.Bookmark
