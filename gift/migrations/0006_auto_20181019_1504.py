# Generated by Django 2.1.1 on 2018-10-19 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0005_auto_20181019_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gifts',
            old_name='gifts_package',
            new_name='gift_package',
        ),
        migrations.RenameField(
            model_name='gifts',
            old_name='gifts_tip',
            new_name='gift_tip',
        ),
    ]