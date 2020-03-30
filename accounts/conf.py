from django.conf import settings as django_settings

settings = {
    'base_template': 'base.html',
    'user_create_fields': (),
    'user_create_required_fields': (),
    'user_create_success_url': '/',
}
settings.update(getattr(django_settings, 'DJANGO_ACCOUNTS', {}))
