from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl

class UserProfileConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.user_profile"
    verbose_name = gl('User Profile')
