# Generated by Django 2.1.1 on 2018-10-08 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vein', '0004_apply_status_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='relation_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vein.TagRelation'),
        ),
    ]
