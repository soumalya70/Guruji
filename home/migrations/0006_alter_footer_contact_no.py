# Generated by Django 4.1.4 on 2023-03-11 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_remove_footer_social_media_links_footer_facebook_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footer", name="contact_no", field=models.IntegerField(),
        ),
    ]
