# Generated by Django 3.0.4 on 2020-04-07 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200406_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_id',
            new_name='number',
        ),
    ]