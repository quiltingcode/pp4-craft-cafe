# Generated by Django 3.2.16 on 2023-02-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_rename_craft_categories_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]