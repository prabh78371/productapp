# Generated by Django 4.0.2 on 2022-03-09 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
