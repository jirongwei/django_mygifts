# Generated by Django 2.1.1 on 2018-10-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0013_delete_giftsdetailpic'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftscomment',
            name='credit',
            field=models.SmallIntegerField(default=1),
        ),
    ]