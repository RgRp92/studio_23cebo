from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page1(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page1Risk_Pref(Page):
    form_model = 'player'
    form_fields = ['q_risk1','q_risk2','q_risk3','q_risk4','q_risk5','q_risk6','q_risk7']

class Page2Time_Pref(Page):
        form_model = 'player'
        form_fields = ['time_1', 'time_2', 'time_3', 'time_4',
                       'time_5']

class Page3Loss_Aversion(Page):
    form_model = 'player'
    form_fields = ['q_loss1', 'q_loss2', 'q_loss3', 'q_loss4',
                   'q_loss5', 'q_loss6',  ]

class Results(Page):
    form_model = 'player'

page_sequence = [Page0,
                 Page1Risk_Pref,
                 Page2Time_Pref,
                 Page3Loss_Aversion]
