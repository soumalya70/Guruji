# Generated by Django 4.1.4 on 2023-03-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="description",
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name="description",
            name="description",
            field=models.TextField(max_length=255),
        ),
    ]
