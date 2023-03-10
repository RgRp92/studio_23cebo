# Generated by Django 2.2.12 on 2023-02-22 11:33

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase4', '0006_auto_20230222_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='q7_g1',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='q7_g2',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='q7_g3',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='q8_g1',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='q8_g2',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='q8_g3',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True),
        ),
    ]
