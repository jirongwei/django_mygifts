# Generated by Django 2.1.1 on 2018-10-18 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0002_auto_20181018_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifts',
            name='day_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gift.GiftsFestival'),
        ),
    ]
