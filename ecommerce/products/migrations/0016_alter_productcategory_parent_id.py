# Generated by Django 4.2.11 on 2024-03-21 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_productcategory_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory'),
        ),
    ]