# Generated by Django 2.1.1 on 2018-10-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0004_auto_20181018_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gifts',
            old_name='field03',
            new_name='gifts_tip',
        ),
        migrations.AddField(
            model_name='gifts',
            name='gifts_package',
            field=models.CharField(max_length=100, null=True),
        ),
    ]