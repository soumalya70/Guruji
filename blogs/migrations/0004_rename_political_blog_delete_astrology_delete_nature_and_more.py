# Generated by Django 4.1.7 on 2023-04-10 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0003_astrology_image_astrology_long_description1_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="Political", new_name="Blog",),
        migrations.DeleteModel(name="Astrology",),
        migrations.DeleteModel(name="Nature",),
        migrations.DeleteModel(name="Religious",),
        migrations.DeleteModel(name="Social",),
        migrations.DeleteModel(name="Sports",),
    ]
