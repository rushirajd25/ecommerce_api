# Generated by Django 4.2.11 on 2024-03-16 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_media_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='product_media/%d%b%Y:%H:%M:%S:%f/'),
        ),
    ]
