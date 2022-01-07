from django.db import models

from django.conf.global_settings import LANGUAGES

class ModelWithLanguage(models.Model):
    language = models.CharField(max_length=7, choices=LANGUAGES)
