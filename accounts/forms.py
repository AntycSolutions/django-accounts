from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model

from accounts.conf import settings


User = get_user_model()


class AuthenticationForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['autofocus'] = True


class UserCreationForm(auth_forms.UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        ) + settings['user_create_fields']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        user_create_required_fields = settings['user_create_required_fields']
        if user_create_required_fields:
            for field in self.fields:
                if field in user_create_required_fields:
                    self.fields[field].required = True
