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
    name_in_url = 'Fase1NEW'
    num_rounds = 1
    players_per_group = None
    app_name = 'Fase1NEW'
    variation = random.randint(1, 100)


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
    income1 = models.FloatField(default=0, min=1, label="")
    income2 = models.FloatField(default=0, min=1, label="")
    income3 = models.FloatField(default=0, min=1, label="")
    avginc = models.FloatField(default=0, min=1, label="")

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


    w_amt = models.FloatField(default=0,min=0,label="")

    def set_winning_bin(self):

        if Constants.variation <= 7:
            self.participant.vars['nw_bin'] = "3"
        elif Constants.variation > 7 and Constants.variation <= 21:
            self.participant.vars['nw_bin'] = "4"
        elif Constants.variation > 21 and Constants.variation<= 60:
            self.participant.vars['nw_bin'] = "5"
        elif  Constants.variation > 60 and Constants.variation<= 74:
            self.participant.vars['nw_bin'] = "6"
        elif Constants.variation > 74 and Constants.variation<= 87:
            self.participant.vars['nw_bin'] = "7"
        elif Constants.variation > 87 and Constants.variation <= 99:
            self.participant.vars['nw_bin'] = "8"
        elif Constants.variation > 99 and Constants.variation <= 100:
            self.participant.vars['nw_bin'] = "9"
