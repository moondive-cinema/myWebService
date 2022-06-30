from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", PostLV.as_view(), name="index"),
    path("post", PostLV.as_view(), name="post_list"),
    path("archive", PostAV.as_view(), name="post_archive"),
    path("<str:slug>", PostDV.as_view(), name="post_detail"),
    path("archive/<int:year>", PostYAV.as_view(), name="post_year_archive"),
    path(
        "archive/<int:year>/<int:month>", PostMAV.as_view(), name="post_month_archive"
    ),
]
