# Generated by Django 2.1.1 on 2018-10-08 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]