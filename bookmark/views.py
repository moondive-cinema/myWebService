from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Bookmark


# 북마크 리스트 뷰 bk_list
class BookmarkLV(ListView):
    model = Bookmark
    paginate_by = 10
    paginate_orphans = 5


# 북마크 디테일 뷰 bk_detail
class BookmarkDV(DetailView):
    model = Bookmark
