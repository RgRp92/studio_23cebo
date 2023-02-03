from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
)

author = 'RR'

doc = """
Beliefs Task
"""
# To read from the CSV file
import pandas as pd
import random

class Constants(BaseConstants):
    name_in_url = 'Fase1_Lite'
    num_rounds = 1
    players_per_group = None
    app_name = 'Fase1_SuperLite'

    # Colors picked with a good pallete
    hex_colors = ["#F8766D", "#00BFC4"]


class Subsession(BaseSubsession):
    def creating_session(self):

        farm_dat = pd.read_csv("farmdata/data.csv")
        self.session.vars["beliefs_farm_dat"] = farm_dat
        self.session.vars["beliefs_hex_colors"] = ["#ff9933", "#00BFC4"]

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    quizf1 = models.CharField(choices=[['2', '4.39 €'],['2', '5.69 €'],['1','7.79 €']],
                               widget= widgets.RadioSelectHorizontal,
                               label='1. In base alla figura mostrata quale sarà il suo guadagno se il reddito varierà tra +1% e +10%?',
                              default = "")
    quiz2f1 = models.CharField(choices=[['2', '3.39 €'],['2', '5.69 €'],['1','7.79 €']],
                            widget=widgets.RadioSelectHorizontal,
                            label='1. In base alla figura mostrata quale sarà il suo guadagno se il reddito varierà tra +1% e +10%?',
                             default="")

    labelset = models.IntegerField(default = 0)

    final_payment = models.StringField()

    bin1  = models.IntegerField(initial = 0)
    bin2  = models.IntegerField(initial = 0)
    bin3  = models.IntegerField(initial = 0)
    bin4  = models.IntegerField(initial = 0)
    bin5  = models.IntegerField(initial = 0)
    bin6  = models.IntegerField(initial = 0)
    bin7  = models.IntegerField(initial = 0)
    bin8  = models.IntegerField(initial = 0)
    bin9  = models.IntegerField(initial = 0)
    bin10  = models.IntegerField(initial = 0)

    rip1 = models.CharField(choices= [['0','Penso che questa allocazione rispecchi accuratamente la mia opinione, non voglio procedere con altre allocazioni']
                                      ,['1','Voglio procedere con una seconda allocazione']],label="",
                                      widget = widgets.RadioSelectHorizontal, default="")


    rip2 = models.CharField(choices= [['0','Penso che questa allocazione rispecchi accuratamente la mia opinione, non voglio procedere con altre allocazioni']
                                      ,['1','Voglio procedere con una terza allocazione']],label="",
                                      widget = widgets.RadioSelectHorizontal, default="")

    pref1 = models.IntegerField(choices=[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],default = 6, min=1, max=10, initial=6, label="")
    pref2 = models.IntegerField(choices=[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],default = 6, min=1, max=10, initial=6, label="")
    pref3 = models.IntegerField(choices=[ 1, 2, 3, 4, 5, 6, 7, 8, 9,10],default = 6, min=1, max=10, initial=6, label="")

    sum_token = models.FloatField(initial=18,default= 18,min=3, max=30)

    w_amt = models.FloatField(default=0,min=0,label="")

    def set_winning_bin(self):
        self.participant.vars['variation'] = random.randint(1, 100)

        if self.participant.vars['variation'] <= 30:
            self.participant.vars['nw_bin'] = "1"
        elif self.participant.vars['variation'] > 30 and self.participant.vars['variation'] <= 54:
            self.participant.vars['nw_bin'] = "2"
        elif self.participant.vars['variation'] > 54 and self.participant.vars['variation']<= 73:
            self.participant.vars['nw_bin'] = "3"
        elif  self.participant.vars['variation'] > 73 and self.participant.vars['variation']<= 88:
            self.participant.vars['nw_bin'] = "4"
        elif self.participant.vars['variation'] > 88 and self.participant.vars['variation']<= 100:
            self.participant.vars['nw_bin'] = "5"
