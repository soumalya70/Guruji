# Generated by Django 4.1.7 on 2023-04-10 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0005_remove_guruji_description_remove_guruji_guruji_image"),
    ]

    operations = [
        migrations.DeleteModel(name="Guruji",),
    ]
