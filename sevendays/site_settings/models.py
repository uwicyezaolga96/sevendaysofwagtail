from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    twitter = models.URLField(blank=True, max_length=100)

    panels = [FieldPanel("twitter")]
