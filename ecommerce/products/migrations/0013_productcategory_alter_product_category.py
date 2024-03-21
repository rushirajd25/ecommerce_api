# Generated by Django 4.2.11 on 2024-03-19 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_rename_media_productmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
    ]
