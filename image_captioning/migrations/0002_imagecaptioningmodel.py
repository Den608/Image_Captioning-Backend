# Generated by Django 4.1.5 on 2023-08-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("image_captioning", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImageCaptioningModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
