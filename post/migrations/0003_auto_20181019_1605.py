# Generated by Django 2.1.1 on 2018-10-19 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20181016_1516'),
        ('post', '0002_postcollect_postthumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRContent', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PostReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prTName', models.CharField(max_length=30)),
                ('prTContent', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='p_status',
            field=models.SmallIntegerField(choices=[(0, '不显示'), (1, '显示')], default=1),
        ),
        migrations.AddField(
            model_name='postreport',
            name='PRType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.PostReportType'),
        ),
        migrations.AddField(
            model_name='postreport',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
        migrations.AddField(
            model_name='postreport',
            name='userinfo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]
