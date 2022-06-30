from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Blog Post",
            {
                "fields": (
                    "title",
                    "author",
                    "slug",
                    "created_date",
                    "description",
                    "content",
                )
            },
        ),
    )

    list_display = ("title", "author", "created_date", "modified_date")
    list_filter = (
        "created_date",
        "author",
    )
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
