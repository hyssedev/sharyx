import os
from django.db import models
from sharyx.settings import UPLOADS_DIR

# Create your models here.

class Uploads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    uploaded_file = models.FileField(upload_to=UPLOADS_DIR)