from taggit.models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.dates import (
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
    TodayArchiveView,
)
from config.views import OwnerOnlyMixin
from .models import Post
from .forms import PostSearchForm


class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["disqus_short"] = f"{settings.DISQUS_SHORTNAME}"
        context["disqus_id"] = f"post-{self.object.id}-{self.object.slug}"
        context[
            "disqus_url"
        ] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context["disqus_title"] = f"{self.object.slug}"
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "description", "content", "tags"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostChangeLV(LoginRequiredMixin, ListView):
    template_name = "blog/post_change_list.html"

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields = ["title", "description", "content", "tags"]
    success_url = reverse_lazy("blog:index")


class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:index")


class PostAV(ArchiveIndexView):
    model = Post
    date_field = "modify_dt"


class PostYAV(YearArchiveView):
    model = Post
    date_field = "modify_dt"
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = "modify_dt"


class PostDAV(DayArchiveView):
    model = Post
    date_field = "modify_dt"


class PostTAV(TodayArchiveView):
    model = Post
    date_filed = "modify_dt"


class TagCloudTV(TemplateView):
    tags = Tag.objects.all()
    context = {"tags": tags}
    template_name = "taggit/taggit_cloud.html"


class TaggedObjectLV(ListView):
    model = Post
    template_name = "taggit/taggit_post_list.html"

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get("tag"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tagname"] = self.kwargs["tag"]
        return context


class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = "blog/post_search.html"

    def form_valid(self, form):
        search_word = form.cleaned_data["search_word"]
        post_list = Post.objects.filter(
            Q(title__icontains=search_word)
            | Q(description__icontains=search_word)
            | Q(content__icontains=search_word)
        ).distinct()
        context = {}
        context["form"] = form
        context["search_term"] = search_word
        context["object_list"] = post_list

        return render(self.request, self.template_name, context)
