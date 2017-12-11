from django.views import generic
from django.contrib.auth import get_user_model

from accounts.conf import settings


base_template = settings['base_template']


User = get_user_model()


class UserDetail(generic.DetailView):
    model = User
    template_name = "accounts/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['base_template'] = base_template

        return context
