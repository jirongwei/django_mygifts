# Generated by Django 2.1.1 on 2018-10-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0014_giftscomment_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftscomment',
            name='comment_time',
            field=models.FloatField(null=True),
        ),
    ]