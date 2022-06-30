from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
)
from .models import Post


class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 10


class PostDV(DetailView):
    model = Post
    context_object_name = "post"


class PostAV(ArchiveIndexView):
    model = Post
    date_field = "created_date"


class PostYAV(YearArchiveView):
    model = Post
    date_field = "created_date"
    context_object_name = "yearly_posts"
    make_object_list = True
    month_format = "%m"  # Invalid date string "2022__5__" given format "%Y__%b__" 애러 해결을 위해 month_format 추가함


class PostMAV(MonthArchiveView):
    model = Post
    date_field = "created_date"
    context_object_name = "monthly_posts"
    make_object_list = True
    month_format = "%m"
