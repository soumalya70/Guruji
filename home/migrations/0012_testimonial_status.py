# Generated by Django 4.1.4 on 2023-03-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_aaj_ka_rashifal_delete_todayshoroscope"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial_status",
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
                ("Happy_Clients", models.IntegerField()),
                ("Services_Available", models.IntegerField()),
                ("Happy_Family", models.IntegerField()),
            ],
        ),
    ]
