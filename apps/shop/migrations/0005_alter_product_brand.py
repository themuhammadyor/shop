# Generated by Django 5.0.6 on 2024-05-20 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_brand_alter_category_cover_remove_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
