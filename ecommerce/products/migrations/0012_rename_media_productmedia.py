# Generated by Django 4.2.11 on 2024-03-19 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_media_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Media',
            new_name='ProductMedia',
        ),
    ]