import os
from django.db import models
from sharyx.settings import UPLOADS_DIR
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.

# deleting files when deleting entries in the database
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)

def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)

class Uploads(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    uploaded_file = models.FileField(upload_to=UPLOADS_DIR)
    delete_code = models.CharField(max_length=6)