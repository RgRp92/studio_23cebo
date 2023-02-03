# Generated by Django 2.2.12 on 2023-01-27 23:13

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase_likert_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Fase_Likert_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fase_likert_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Fase_Likert_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('q_risk1', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk2', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk3', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk4', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk5', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk6', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('q_risk7', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Risk')),
                ('time_1', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('time_2', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('time_3', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('time_4', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('time_5', otree.db.models.IntegerField(choices=[[1, 'A'], [2, 'B']], default=0, null=True)),
                ('q_time1', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time2', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time3', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time4', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time5', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time6', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_time7', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Cooperazione')),
                ('q_loss1', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss2', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss3', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss4', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss5', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss6', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('q_loss7', otree.db.models.StringField(choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']], max_length=10000, null=True, verbose_name='Assimetria Informativa')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Fase_Likert.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase_likert_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fase_likert_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fase_Likert.Subsession')),
            ],
            options={
                'db_table': 'Fase_Likert_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fase_Likert.Subsession'),
        ),
    ]