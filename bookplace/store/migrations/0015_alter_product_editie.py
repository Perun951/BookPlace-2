# Generated by Django 4.1.6 on 2023-02-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='editie',
            field=models.IntegerField(max_length=50),
        ),
    ]