# Generated by Django 4.2 on 2023-04-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=False, upload_to='Product'),
        ),
    ]
