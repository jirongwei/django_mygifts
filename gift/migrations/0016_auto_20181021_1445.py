# Generated by Django 2.1.1 on 2018-10-21 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20181016_1516'),
        ('gift', '0015_giftscomment_comment_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftsorder',
            name='field02',
        ),
        migrations.AddField(
            model_name='giftsorder',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Address'),
        ),
    ]