from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random



class Winner(Page):

    def vars_for_template(self):
        return {
        'app' : self.session.vars["app"],
        'id':   self.player.id_in_group
        }


class ResultsWaitPage(WaitPage):
    pass

class Fase1(Page):
    def vars_for_template(self):
        return{
        "beliefs": self.participant.vars["beliefs_results"],
        "w_amt": self.participant.vars["w_amt"],
        "nw_bin": self.participant.vars["nw_bin"]
        }

    def is_displayed(self):
        return self.session.vars["app"] == 1

    def before_next_page(self):
        self.player.payoff = round(self.participant.vars["w_amt"],2)

class Fase2(Page):
    def vars_for_template(self):

        return {
            'player_in_all_rounds': self.player.in_all_rounds(),
            'box_value': self.participant.vars['box_value'],
            'boxes_total': self.participant.vars['boxes_total'],
            'boxes_collected': self.participant.vars['boxes_collected'],
            'bomb': self.participant.vars['bomb'],
            'bomb_row': self.participant.vars['bomb_row'],
            'bomb_col': self.participant.vars['bomb_col'] ,
            'round_result': self.participant.vars['round_result'],
            'round_to_pay':  self.participant.vars['round_to_pay'],
            'payoff': self.participant.vars['payoff'],
            'total_payoff':self.participant.vars['payoff'],
        }

    def is_displayed(self):
        return self.session.vars["app"] == 2

    def before_next_page(self):
        self.player.payoff = (self.player.participant.vars['bret_payoff'])

class Fase3(Page):
    def vars_for_template(self):
        payoff_rHLc = round((self.player.participant.vars['payoff_rHL']/1000) * (1.06),2)
        # retrieve values from participant.vars and store them in a dictionary
            # retrieve values from participant.vars and store them in a dictionary
        return {
                'payoff_rHL': self.player.participant.vars['payoff_rHL'],
                'payoff_rHLc': payoff_rHLc,  # payoff
                'rrow': self.player.participant.vars['rHL_row'],  # randomly chosen row
                'rvalue': self.participant.vars['rHL_random'],  # randomly chosen value to define outcome
                'rchoice': self.participant.vars['HL_choice_rs1'],  # actual choice
                # outcomes of the selected row
                'ra1_value': self.participant.vars['ra1_value'],
                'ra2_value': self.participant.vars['ra2_value'],
                'ra3_value': self.participant.vars['ra3_value'],
                'ra4_value': self.participant.vars['ra4_value'],
                'ra5_value': self.participant.vars['ra5_value'],
                'rb1_value': self.participant.vars['rb1_value'],
                'rb2_value': self.participant.vars['rb2_value'],
                'rb3_value': self.participant.vars['rb3_value'],
                'rb4_value': self.participant.vars['rb4_value'],
                'rb5_value': self.participant.vars['rb5_value'],
                'p_A_1': self.participant.vars['rHL_row'],
                'p_A_2': 10 - self.participant.vars['rHL_row'],
                'p_B_1': self.participant.vars['rHL_row'],
                'p_B_2': 10 - self.participant.vars['rHL_row'],
                'var1': self.participant.vars['var1'] * 100,
                'var11': self.participant.vars['var11'] * 100,
                'var2': self.participant.vars['var2'] * 100,
                'var22': self.participant.vars['var22'] * 100,
                'var3': self.participant.vars['var3'] * 100,
                'var33': self.participant.vars['var33'] * 100,
                'var4': self.participant.vars['var4'] * 100,
                'var44': self.participant.vars['var44'] * 100,
                'var5': self.participant.vars['var5'] * 100,
                'var55': self.participant.vars['var55'] * 100,

                'rist_value': self.participant.vars['rist_value'],
                'prb1': self.participant.vars['prb1'],
                'prb2': self.participant.vars['prb2'],
                'prb3': self.participant.vars['prb3'],
                'prb4': self.participant.vars['prb4'],
                'prb5': self.participant.vars['prb5'],
        }

    def is_displayed(self):
        return self.session.vars["app"] == 3

    def before_next_page(self):
        self.player.payoff = round((self.player.participant.vars['payoff_rHL']/1000) * (1.06),2)


class goodbye(Page):
    form_model = 'player'

    def vars_for_template(self):
        return {
        'id':   self.player.id_in_group
        }

page_sequence = [Winner, Fase1, Fase2, Fase3, goodbye]
