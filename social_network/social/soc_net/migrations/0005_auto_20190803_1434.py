# Generated by Django 2.2.4 on 2019-08-03 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0004_post_users_reaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='users_reaction',
        ),
    ]
