# Generated by Django 2.1.1 on 2018-10-18 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0013_auto_20181016_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=32)),
                ('ptitleimg', models.CharField(max_length=200, null=True)),
                ('pdetailcont', models.CharField(max_length=9000)),
                ('pbriefcont', models.CharField(max_length=900)),
                ('p_createtime', models.IntegerField()),
                ('p_userid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='PostReply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pReply_con', models.CharField(max_length=120)),
                ('pReply_reply', models.IntegerField(null=True)),
                ('pReply_time', models.IntegerField()),
                ('pReply_pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('pReply_uid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
    ]