# Generated by Django 2.2.12 on 2023-02-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fase4', '0005_auto_20230211_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='qred1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='qred2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='qred3',
        ),
    ]
