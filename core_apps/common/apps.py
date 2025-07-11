from django.apps import AppConfig
from django.utils.translation import gettext_lazy as gl

class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.common"
    verbose_name = gl('Common')