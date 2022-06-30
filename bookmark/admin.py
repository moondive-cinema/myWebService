from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "description")


admin.site.register(Bookmark, BookmarkAdmin)
