# Generated by Django 4.1.1 on 2022-10-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_uploads_delete_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='delete_code',
            field=models.CharField(max_length=13),
        ),
    ]