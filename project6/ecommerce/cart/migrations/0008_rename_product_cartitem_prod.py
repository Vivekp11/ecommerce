# Generated by Django 4.2.5 on 2023-10-24 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_rename_prod_cartitem_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='prod',
        ),
    ]