# Generated by Django 2.1.1 on 2018-10-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0007_gifts_new_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifts',
            name='gift_material',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
