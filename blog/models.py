from django.utils import timezone
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("TITLE", max_length=50)
    slug = models.SlugField(
        "SLUG", unique=True, allow_unicode=True, help_text="one word for title alias"
    )
    author = models.CharField(
        "AUTHOR", max_length=50, blank=True, help_text="author of the content"
    )
    description = models.CharField(
        "DESCRIPTION", max_length=140, blank=True, help_text="simple description text"
    )
    content = models.TextField("CONTENT")
    created_date = models.DateTimeField("CREATED", default=timezone.now) # admin 패이지에서 생성일 변경이 가능하게 하기 위해 auto_now_add를 사용안함
    modified_date = models.DateTimeField("MODIFIED", auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        db_table = "my_post"  # 지정하지 않으면 앱명_모델명으로 DB테이블에 저장됨 (blog_post)
        ordering = ("-created_date",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_created_date()

    def get_next_post(self):
        return self.get_next_by_created_date()
