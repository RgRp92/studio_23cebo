from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random




class Page0(Page):


    def is_displayed(self):
        return self.round_number == 1

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage2(Page):
    form_model = 'player'

class IstruzioniPage3(Page):
    form_model = 'player'
    def vars_for_template(self):
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5

        return {
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55}

class EsempioPage1(Page):
# which forms are needed from class player
    form_model = 'player'
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        return {
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
             'var5': var5,
            'var55': var55,

        }


    # values that are to be displayed (dictionary)
    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)

class MyWaitPage(Page):
    form_model = 'player'


    def vars_for_template(self):
        self.player.vars_for_template()
        rrate = round(25000 / self.participant.vars['inc5r'], 2)
        return {'rrate': rrate}

    def before_next_page(self):
        self.participant.vars['rrate'] = round(25000 / self.participant.vars['inc5r'], 2)


class HL_Page1(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['rHL_1',
                   'rHL_2',
                   'rHL_3',
                   'rHL_4',
                   'rHL_5',
                   'rHL_6',
                   'rHL_7',
                   'rHL_8',
                   'rHL_9',
                   'rHL_10','rHL_11','rHL_12',
                   ] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        var1 = Constants.var1 * 100
        var11 = Constants.var11 * 100
        var2 = Constants.var2 * 100
        var22 = Constants.var22 * 100
        var3 = Constants.var3 * 100
        var33 = Constants.var33 * 100
        var4 = Constants.var4 * 100
        var44 = Constants.var44 * 100
        var5 = Constants.var5 * 100
        var55 = Constants.var55 * 100

        prb1 = Constants.prb1
        prb2 = Constants.prb2
        prb3 = Constants.prb3
        prb4 = Constants.prb4
        prb5 = Constants.prb5
        return {
            'prb1': prb1,
            'prb2': prb2,
            'prb3': prb3,
            'prb4': prb4,
            'prb5': prb5,

            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55,

            'ist1': self.participant.vars["farmercostr"][0],
            'ist2': self.participant.vars["farmercostr"][1],
            'ist3': self.participant.vars["farmercostr"][2],
            'ist4': self.participant.vars["farmercostr"][3],
            'ist5': self.participant.vars["farmercostr"][4],
            'ist6': self.participant.vars["farmercostr"][5],
            'ist7': self.participant.vars["farmercostr"][6],
            'ist8': self.participant.vars["farmercostr"][7],
            'ist9': self.participant.vars["farmercostr"][8],
            'ist10': self.participant.vars["farmercostr"][9],
            'ist11': self.participant.vars["farmercostr"][10],
            'ist12': self.participant.vars["farmercostr"][11],

            'a': self.participant.vars['inc1r'],
            'a_1': self.participant.vars['inc_ar'][0],
            'a_2': self.participant.vars['inc_ar'][1],
            'a_3': self.participant.vars['inc_ar'][2],
            'a_4': self.participant.vars['inc_ar'][3],
            'a_5': self.participant.vars['inc_ar'][4],
            'a_6': self.participant.vars['inc_ar'][5],
            'a_7': self.participant.vars['inc_ar'][6],
            'a_8': self.participant.vars['inc_ar'][7],
            'a_9': self.participant.vars['inc_ar'][8],
            'a_10': self.participant.vars['inc_ar'][9],
            'a_11': self.participant.vars['inc_ar'][10],
            'a_12': self.participant.vars['inc_ar'][11],

            'b': self.participant.vars['inc2r'],
            'b_1': self.participant.vars['inc_br'][0],
            'b_2': self.participant.vars['inc_br'][1],
            'b_3': self.participant.vars['inc_br'][2],
            'b_4': self.participant.vars['inc_br'][3],
            'b_5': self.participant.vars['inc_br'][4],
            'b_6': self.participant.vars['inc_br'][5],
            'b_7': self.participant.vars['inc_br'][6],
            'b_8': self.participant.vars['inc_br'][7],
            'b_9': self.participant.vars['inc_br'][8],
            'b_10': self.participant.vars['inc_br'][9],
            'b_11': self.participant.vars['inc_br'][10],
            'b_12': self.participant.vars['inc_br'][11],

            'c': self.participant.vars['inc3r'],
            'c_1': self.participant.vars['inc_cr'][0],
            'c_2': self.participant.vars['inc_cr'][1],
            'c_3': self.participant.vars['inc_cr'][2],
            'c_4': self.participant.vars['inc_cr'][3],
            'c_5': self.participant.vars['inc_cr'][4],
            'c_6': self.participant.vars['inc_cr'][5],
            'c_7': self.participant.vars['inc_cr'][6],
            'c_8': self.participant.vars['inc_cr'][7],
            'c_9': self.participant.vars['inc_cr'][8],
            'c_10': self.participant.vars['inc_cr'][9],
            'c_11': self.participant.vars['inc_cr'][10],
            'c_12': self.participant.vars['inc_cr'][11],

            'd': self.participant.vars['inc4r'],
            'd_1': self.participant.vars['inc_dr'][0],
            'd_2': self.participant.vars['inc_dr'][1],
            'd_3': self.participant.vars['inc_dr'][2],
            'd_4': self.participant.vars['inc_dr'][3],
            'd_5': self.participant.vars['inc_dr'][4],
            'd_6': self.participant.vars['inc_dr'][5],
            'd_7': self.participant.vars['inc_dr'][6],
            'd_8': self.participant.vars['inc_dr'][7],
            'd_9': self.participant.vars['inc_dr'][8],
            'd_10': self.participant.vars['inc_dr'][9],
            'd_11': self.participant.vars['inc_dr'][10],
            'd_12': self.participant.vars['inc_dr'][11],

            'e': self.participant.vars['inc5r'],
            'e_1': self.participant.vars['inc_er'][0],
            'e_2': self.participant.vars['inc_er'][1],
            'e_3': self.participant.vars['inc_er'][2],
            'e_4': self.participant.vars['inc_er'][3],
            'e_5': self.participant.vars['inc_er'][4],
            'e_6': self.participant.vars['inc_er'][5],
            'e_7': self.participant.vars['inc_er'][6],
            'e_8': self.participant.vars['inc_er'][7],
            'e_9': self.participant.vars['inc_er'][8],
            'e_10': self.participant.vars['inc_er'][9],
            'e_11': self.participant.vars['inc_er'][10],
            'e_12': self.participant.vars['inc_er'][11],

            'diff_a1': (-1 * self.participant.vars["diff1r"][0]),
            'diff_b1': self.participant.vars["diff1r"][1],
            'diff_a2': (-1 * self.participant.vars["diff2r"][0]),
            'diff_b2': self.participant.vars["diff2r"][1],
            'diff_a3': (-1 * self.participant.vars["diff3r"][0]),
            'diff_b3': self.participant.vars["diff3r"][1],
            'diff_a4': (-1 * self.participant.vars["diff4r"][0]),
            'diff_b4': self.participant.vars["diff4r"][1],
            'diff_a5': (-1 * self.participant.vars["diff5r"][0]),
            'diff_b5': self.participant.vars["diff5r"][1],
            'diff_a6': (-1 * self.participant.vars["diff6r"][0]),
            'diff_b6': self.participant.vars["diff6r"][1],
            'diff_a7': (-1 * self.participant.vars["diff7r"][0]),
            'diff_b7': self.participant.vars["diff7r"][1],
            'diff_a8': (-1 * self.participant.vars["diff8r"][0]),
            'diff_b8': self.participant.vars["diff8r"][1],
            'diff_a9': (-1 * self.participant.vars["diff9r"][0]),
            'diff_b9': self.participant.vars["diff9r"][1],
            'diff_a10': (-1 * self.participant.vars["diff10r"][0]),
            'diff_b10': self.participant.vars["diff10r"][1],
            'diff_a11': (-1 * self.participant.vars["diff11r"][0]),
            'diff_b11': self.participant.vars["diff11r"][1],
            'diff_a12': (-1 * self.participant.vars["diff12r"][0]),
            'diff_b12': self.participant.vars["diff12r"][1],

        }

# before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)

    def before_next_page(self):
            self.player.set_payoff_HLr()  # see in models in Player class
            self.participant.vars['a1_valuer'] = self.participant.vars['inc_ar'][self.participant.vars['HL_rowr'] - 1]
            self.participant.vars['a2_valuer'] = self.participant.vars['inc_br'][self.participant.vars['HL_rowr'] - 1]
            self.participant.vars['a3_valuer'] = self.participant.vars['inc_cr'][self.participant.vars['HL_rowr'] - 1]
            self.participant.vars['a4_valuer'] = self.participant.vars['inc_dr'][self.participant.vars['HL_rowr'] - 1]
            self.participant.vars['a5_valuer'] = self.participant.vars['inc_er'][self.participant.vars['HL_rowr'] - 1]

            self.participant.vars['b1_valuer'] = self.participant.vars['inc1r']
            self.participant.vars['b2_valuer'] = self.participant.vars['inc2r']
            self.participant.vars['b3_valuer'] = self.participant.vars['inc3r']
            self.participant.vars['b4_valuer'] = self.participant.vars['inc4r']
            self.participant.vars['b5_valuer'] = self.participant.vars['inc5r']

            self.participant.vars['var1'] = Constants.var1
            self.participant.vars['var11'] = Constants.var11
            self.participant.vars['var2'] = Constants.var2
            self.participant.vars['var22'] = Constants.var22
            self.participant.vars['var3'] = Constants.var3
            self.participant.vars['var33'] = Constants.var33
            self.participant.vars['var4'] = Constants.var4
            self.participant.vars['var44'] = Constants.var44
            self.participant.vars['var5'] = Constants.var5
            self.participant.vars['var55'] = Constants.var55

            self.participant.vars['prb1'] = Constants.prb1
            self.participant.vars['prb2'] = Constants.prb2
            self.participant.vars['prb3'] = Constants.prb3
            self.participant.vars['prb4'] = Constants.prb4
            self.participant.vars['prb5'] = Constants.prb5

class OutcomeHL(Page):
    # values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return {
            'payoff_rHL': self.player.participant.vars['payoff_HLr'],  # payoff
            'rrow': self.player.participant.vars['HL_rowr'],  # randomly chosen row
            'rvalue': self.participant.vars['HL_randomr'],  # randomly chosen value to define outcome
            'rvalue2': self.participant.vars['HL_scenarior'],
            'rchoice': self.participant.vars['HL_choice_rs1'],  # actual choice
            # outcomes of the selected row
            'ra1_value': self.participant.vars['inc_ar'][self.participant.vars['HL_rowr'] - 1],
            'ra2_value': self.participant.vars['inc_br'][self.participant.vars['HL_rowr'] - 1],
            'ra3_value': self.participant.vars['inc_cr'][self.participant.vars['HL_rowr'] - 1],
            'ra4_value': self.participant.vars['inc_dr'][self.participant.vars['HL_rowr'] - 1],
            'ra5_value': self.participant.vars['inc_er'][self.participant.vars['HL_rowr'] - 1],

            'rb1_value': self.participant.vars['inc1r'],
            'rb2_value': self.participant.vars['inc2r'],
            'rb3_value': self.participant.vars['inc3r'],
            'rb4_value': self.participant.vars['inc4r'],
            'rb5_value': self.participant.vars['inc5r'],

            'p_A_1': self.participant.vars['HL_rowr'],
            'p_A_2': 10 - self.participant.vars['HL_rowr'],
            'p_B_1': self.participant.vars['HL_rowr'],
            'p_B_2': 10 - self.participant.vars['HL_rowr'],

            'ist_value':self.participant.vars["farmercostr"][self.participant.vars['HL_rowr'] - 1],

            'var1': -Constants.var1 * 100,
            'var11': -Constants.var11 * 100,
            'var2': -Constants.var2 * 100,
            'var22': -Constants.var22 * 100,
            'var3': -Constants.var3 * 100,
            'var33': Constants.var33 * 100,
            'var4': +Constants.var44 * 100,
            'var44': +Constants.var44 * 100,
            'var5': +Constants.var5 * 100,
            'var55': +Constants.var55 * 100,

        }

    def before_next_page(self):
        self.participant.vars['ist_valuer'] = self.participant.vars["farmercostr"][self.participant.vars['HL_rowr'] - 1]


# the coreography of pages
page_sequence = [
    Page0,
    IstruzioniPage1,
    IstruzioniPage2,
    IstruzioniPage3,
    EsempioPage1,
    MyWaitPage,
    HL_Page1,
    OutcomeHL
]
