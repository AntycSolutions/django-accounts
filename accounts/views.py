from django.views import generic
from django.contrib.auth import get_user_model


User = get_user_model()


class UserDetail(generic.DetailView):
    model = User
    template_name = "accounts/user_detail.html"
