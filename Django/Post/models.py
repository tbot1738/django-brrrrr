from django.db import models
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent


class UserPicHandler(models.Model):
    image = models.ImageField(upload_to="imgs")
