# Generated by Django 4.1.1 on 2022-09-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('uploaded_file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
