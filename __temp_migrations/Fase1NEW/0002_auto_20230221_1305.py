# Generated by Django 2.2.12 on 2023-02-21 12:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='pref1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='pref2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='pref3',
        ),
        migrations.RemoveField(
            model_name='player',
            name='quiz2f1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='quizf1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rip1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rip2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='sum_token',
        ),
        migrations.AddField(
            model_name='player',
            name='avginc',
            field=otree.db.models.FloatField(default=0, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='income1',
            field=otree.db.models.FloatField(default=0, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='income2',
            field=otree.db.models.FloatField(default=0, null=True, verbose_name=''),
        ),
        migrations.AddField(
            model_name='player',
            name='income3',
            field=otree.db.models.FloatField(default=0, null=True, verbose_name=''),
        ),
    ]