# Generated by Django 5.0 on 2023-12-26 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Product',
            new_name='product',
        ),
    ]