# Generated by Django 2.2.4 on 2019-08-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soc_net', '0005_auto_20190803_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
