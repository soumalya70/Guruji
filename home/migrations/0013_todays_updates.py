# Generated by Django 4.1.4 on 2023-03-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_testimonial_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Todays_Updates",
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
                ("image", models.ImageField(upload_to="todays_updates/")),
                ("nakshatra", models.CharField(max_length=150)),
                ("tithi", models.CharField(max_length=150)),
                ("sunrise", models.CharField(max_length=150)),
                ("sunset", models.CharField(max_length=150)),
                ("yoga", models.CharField(max_length=150)),
                ("rashi", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("todays_update", models.TextField()),
            ],
        ),
    ]
