from django.conf import urls
from django.core import urlresolvers
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views


urlpatterns = [
    urls.url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'accounts/login.html'},
        name='login'
    ),
    urls.url(
        r'^logout/$',
        auth_views.logout,
        {'template_name': 'accounts/logout.html'},
        name='logout'
    ),
    urls.url(
        r'^password_change/$',
        auth_views.password_change,
        {
            'template_name': 'accounts/password_change_form.html',
            'post_change_redirect':
                urlresolvers.reverse_lazy('accounts:password_change_done'),
        },
        name='password_change'
    ),
    urls.url(
        r'^password_change/done/$',
        auth_views.password_change_done,
        {'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'
    ),
    urls.url(
        r'^password_reset/$',
        auth_views.password_reset,
        {
            'template_name': 'accounts/password_reset_form.html',
            'email_template_name': 'accounts/password_reset_email.html',
            'post_reset_redirect':
                urlresolvers.reverse_lazy('accounts:password_reset_done'),
        },
        name='password_reset'
    ),
    urls.url(
        r'^password_reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'accounts/password_reset_done.html'},
        name='password_reset_done'),
    urls.url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {
            'template_name': 'accounts/password_reset_confirm.html',
            'post_reset_redirect':
                urlresolvers.reverse_lazy('accounts:password_reset_complete'),
        },
        name='password_reset_confirm'),
    urls.url(
        r'^reset/done/$',
        auth_views.password_reset_complete,
        {'template_name': 'accounts/password_reset_complete.html'},
        name='password_reset_complete'
    ),
    urls.url(
        r'^(?P<pk>\d+)/$',
        accounts_views.UserDetail.as_view(),
        name='user_detail'
    ),
]
