from django.conf import urls
try:
    from django.core import urlresolvers
    carret = '^'
except ImportError:
    from django import urls as urlresolvers
    carret = ''
from django.contrib.auth import views as auth_views, decorators

from accounts import views as accounts_views, forms
from accounts.conf import settings


app_name = 'accounts'
base_template = settings['base_template']

urlpatterns = [
    urls.url(
        r'{}login/$'.format(carret),
        auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            authentication_form=forms.AuthenticationForm,
            extra_context={
                'base_template': base_template
            }
        ),
        name='login'
    ),
    urls.url(
        r'{}logout/$'.format(carret),
        auth_views.LogoutView.as_view(
            template_name='accounts/logout.html',
            extra_context={
                'base_template': base_template
            }
        ),
        name='logout'
    ),
    urls.url(
        r'{}password_change/$'.format(carret),
        auth_views.PasswordChangeView.as_view(
            template_name='accounts/password_change_form.html',
            success_url=(
                urlresolvers.reverse_lazy('accounts:password_change_done')
            ),
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_change'
    ),
    urls.url(
        r'{}password_change/done/$'.format(carret),
        auth_views.PasswordChangeDoneView.as_view(
            template_name='accounts/password_change_done.html',
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_change_done'
    ),
    urls.url(
        r'{}password_reset/$'.format(carret),
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset_form.html',
            email_template_name='accounts/password_reset_email.html',
            success_url=(
                urlresolvers.reverse_lazy('accounts:password_reset_done')
            ),
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_reset'
    ),
    urls.url(
        r'{}password_reset/done/$'.format(carret),
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html',
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_reset_done'),
    urls.url(
        r'{}reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'.format(carret) +
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=(
                urlresolvers.reverse_lazy('accounts:password_reset_complete')
            ),
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_reset_confirm'),
    urls.url(
        r'{}reset/done/$'.format(carret),
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html',
            extra_context={
                'base_template': base_template
            }
        ),
        name='password_reset_complete'
    ),
    urls.url(
        r'{}(?P<pk>\d+)/$'.format(carret),
        decorators.login_required(accounts_views.UserDetail.as_view()),
        name='user_detail'
    ),
]
