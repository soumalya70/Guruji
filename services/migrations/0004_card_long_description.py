# Generated by Django 4.1.7 on 2023-04-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_delete_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="long_description",
            field=models.TextField(default="type here", max_length=400),
        ),
    ]
