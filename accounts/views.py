from django import shortcuts
from django.views import generic
from django.contrib import auth
from django.contrib.auth import get_user_model

from accounts.conf import settings
from accounts import forms


base_template = settings['base_template']


User = get_user_model()


class UserDetail(generic.DetailView):
    model = User
    template_name = "accounts/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['base_template'] = base_template

        return context


class UserCreate(generic.CreateView):
    model = User
    form_class = forms.UserCreationForm
    template_name = 'accounts/user_create.html'
    success_url = settings['user_create_success_url']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['base_template'] = base_template

        return context

    def form_valid(self, form):
        self.object = form.save()
        user = auth.authenticate(
            email=self.object.email, password=form.cleaned_data['password1']
        )
        auth.login(self.request, user)
        return shortcuts.redirect(self.success_url)
