from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Ruggiero Rippo'

doc = """
Fase 4 Questionario
"""


class Constants(BaseConstants):
    name_in_url = 'Fase_Likert'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q_risk1 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk4 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    q_risk7 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Risk',
        widget=widgets.RadioSelectHorizontal,
    )
    time_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    time_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    time_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    time_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    time_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    q_loss2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    q_loss3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    q_loss4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    q_loss6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
