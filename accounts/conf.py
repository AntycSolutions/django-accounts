from django.conf import settings as django_settings

settings = {
    'base_template': 'base.html',
}
settings.update(getattr(django_settings, 'DJANGO_ACCOUNTS', {}))
