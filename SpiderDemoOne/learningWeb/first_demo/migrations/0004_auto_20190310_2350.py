# Generated by Django 2.1.7 on 2019-03-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_demo', '0003_first_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='first',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='first',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]