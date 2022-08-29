from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView


class HomeView(TemplateView):
    template_name = "home.html"


class UserCreateView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("register_done")


class UserCreateDoneTV(TemplateView):
    template_name = "registration/register_done.html"


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "작성자만 수정/삭제 가능합니다."

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
