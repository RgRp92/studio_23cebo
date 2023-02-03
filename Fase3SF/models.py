from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import locale
locale.setlocale(locale.LC_ALL,'')


author = 'Ruggiero Rippo'

doc = """
    MPL risk elicitation à la Tanaka et al 2010
"""

import random

class Constants(BaseConstants):
    name_in_url = 'Fase3SF'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    ist = [150,
           500,
           850,
           880,
           910,
           940,
           961,
           980,
           1000,
           1030,
           1060,
           1100]

    var1 = 0.30
    var11 = 0.20

    var2 = 0.19
    var22 = 0.10

    var3 = 0.09
    var33 = 0.00

    var4 = 0.01
    var44 = 0.10

    var5 = 0.11
    var55 = 0.20

    var6 = 0.21
    var66 = 0.30
    prb1 = 30
    prb2 = 24
    prb3 = 19
    prb4 = 15
    prb5 = 12

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    rHL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_11 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    rHL_12 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)




    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insprem = self.participant.vars['insprem']
        avginc = self.participant.vars['avginc']

        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        disctot = (insvaluedisc + inspremdisc)

        isttot_r1 = round((Constants.ist[0] + inspremist + insvalueist),0)
        isttot_r2 = round((Constants.ist[1] + inspremist + insvalueist),0)
        isttot_r3 = round((Constants.ist[2] + inspremist + insvalueist),0)
        isttot_r4 = round((Constants.ist[3] + inspremist + insvalueist),0)
        isttot_r5 = round((Constants.ist[4] + inspremist + insvalueist),0)
        isttot_r6 = round((Constants.ist[5] + inspremist + insvalueist),0)
        isttot_r7 = round((Constants.ist[6] + inspremist + insvalueist),0)
        isttot_r8 = round((Constants.ist[7] + inspremist + insvalueist),0)
        isttot_r9 = round((Constants.ist[8] + inspremist + insvalueist),0)
        isttot_r10 = round((Constants.ist[9] + inspremist + insvalueist),0)
        isttot_r11 = round((Constants.ist[10] + inspremist + insvalueist),0)
        isttot_r12 = round((Constants.ist[11] + inspremist + insvalueist),0)

        farmercost_1r = round((isttot_r1 - disctot),0)
        farmercost_2r = round((isttot_r2 - disctot),0)
        farmercost_3r = round((isttot_r3 - disctot),0)
        farmercost_4r = round((isttot_r4 - disctot),0)
        farmercost_5r = round((isttot_r5 - disctot),0)
        farmercost_6r = round((isttot_r6 - disctot),0)
        farmercost_7r = round((isttot_r7 - disctot),0)
        farmercost_8r = round((isttot_r8 - disctot),0)
        farmercost_9r = round((isttot_r9 - disctot),0)
        farmercost_10r = round((isttot_r10 - disctot),0)
        farmercost_11r = round((isttot_r11 - disctot),0)
        farmercost_12r = round((isttot_r12 - disctot),0)

        self.participant.vars["farmercostr"] = [farmercost_1r,farmercost_2r,farmercost_3r,farmercost_4r,farmercost_5r,
                                                farmercost_6r,farmercost_7r,farmercost_8r,farmercost_9r,farmercost_10r,
                                                farmercost_11r,farmercost_12r]

        inc1r = round(avginc + (-0.25 * avginc),0)
        loss = avginc - inc1r
        reimb = 0.7 * loss

        inc2r = round(avginc + (-0.15 * avginc),0)
        inc3r = round(avginc + (-0.05 * avginc),0)
        inc4r = round(avginc + (0.05 * avginc),0)
        inc5r = round(avginc + (0.15 * avginc),0)

        self.participant.vars["inc1r"] = inc1r
        self.participant.vars["inc2r"] = inc2r
        self.participant.vars["inc3r"] = inc3r
        self.participant.vars["inc4r"] = inc4r
        self.participant.vars["inc5r"] = inc5r

        inc1_a1r = round(inc1r + reimb - farmercost_1r,0)
        inc1_a2r = round(inc1r + reimb - farmercost_2r,0)
        inc1_a3r = round(inc1r + reimb - farmercost_3r,0)
        inc1_a4r = round(inc1r + reimb - farmercost_4r,0)
        inc1_a5r = round(inc1r + reimb - farmercost_5r,0)
        inc1_a6r = round(inc1r + reimb - farmercost_6r,0)
        inc1_a7r = round(inc1r + reimb - farmercost_7r,0)
        inc1_a8r = round(inc1r + reimb - farmercost_8r,0)
        inc1_a9r = round(inc1r + reimb - farmercost_9r,0)
        inc1_a10r = round(inc1r + reimb - farmercost_10r,0)
        inc1_a11r = round(inc1r + reimb - farmercost_11r,0)
        inc1_a12r = round(inc1r + reimb - farmercost_12r,0)

        self.participant.vars["inc_ar"] = [inc1_a1r,inc1_a2r,inc1_a3r,inc1_a4r,inc1_a5r,inc1_a6r,
                                          inc1_a7r,inc1_a8r,inc1_a9r,inc1_a10r,inc1_a11r,inc1_a12r,]

        inc1_b1r = round(inc2r - farmercost_1r,0)
        inc1_b2r = round(inc2r - farmercost_2r,0)
        inc1_b3r = round(inc2r - farmercost_3r,0)
        inc1_b4r = round(inc2r - farmercost_4r,0)
        inc1_b5r = round(inc2r - farmercost_5r,0)
        inc1_b6r = round(inc2r - farmercost_6r,0)
        inc1_b7r = round(inc2r - farmercost_7r,0)
        inc1_b8r = round(inc2r - farmercost_8r,0)
        inc1_b9r = round(inc2r - farmercost_9r,0)
        inc1_b10r = round(inc2r - farmercost_10r,0)
        inc1_b11r = round(inc2r - farmercost_11r,0)
        inc1_b12r = round(inc2r - farmercost_12r,0)

        self.participant.vars["inc_br"] = [inc1_b1r, inc1_b2r, inc1_b3r, inc1_b4r, inc1_b5r, inc1_b6r,
                                          inc1_b7r, inc1_b8r, inc1_b9r, inc1_b10r, inc1_b11r, inc1_b12r, ]

        inc1_c1r = round(inc3r - farmercost_1r,0)
        inc1_c2r = round(inc3r - farmercost_2r,0)
        inc1_c3r = round(inc3r - farmercost_3r,0)
        inc1_c4r = round(inc3r - farmercost_4r,0)
        inc1_c5r = round(inc3r - farmercost_5r,0)
        inc1_c6r = round(inc3r - farmercost_6r,0)
        inc1_c7r = round(inc3r - farmercost_7r,0)
        inc1_c8r = round(inc3r - farmercost_8r,0)
        inc1_c9r = round(inc3r - farmercost_9r,0)
        inc1_c10r = round(inc3r - farmercost_10r,0)
        inc1_c11r = round(inc3r - farmercost_11r,0)
        inc1_c12r = round(inc3r - farmercost_12r,0)

        self.participant.vars["inc_cr"] = [inc1_c1r, inc1_c2r, inc1_c3r, inc1_c4r, inc1_c5r, inc1_c6r,
                                          inc1_c7r, inc1_c8r, inc1_c9r, inc1_c10r, inc1_c11r, inc1_c12r, ]

        inc1_d1r = round(inc4r - farmercost_1r,0)
        inc1_d2r = round(inc4r - farmercost_2r,0)
        inc1_d3r = round(inc4r - farmercost_3r,0)
        inc1_d4r = round(inc4r - farmercost_4r,0)
        inc1_d5r = round(inc4r - farmercost_5r,0)
        inc1_d6r = round(inc4r - farmercost_6r,0)
        inc1_d7r = round(inc4r - farmercost_7r,0)
        inc1_d8r = round(inc4r - farmercost_8r,0)
        inc1_d9r = round(inc4r - farmercost_9r,0)
        inc1_d10r = round(inc4r - farmercost_10r,0)
        inc1_d11r = round(inc4r - farmercost_11r,0)
        inc1_d12r = round(inc4r - farmercost_12r,0)

        self.participant.vars["inc_dr"] = [inc1_d1r, inc1_d2r, inc1_d3r, inc1_d4r, inc1_d5r, inc1_d6r,
                                          inc1_d7r, inc1_d8r, inc1_d9r, inc1_d10r, inc1_d11r, inc1_d12r, ]

        inc1_e1r = round(inc5r - farmercost_1r,0)
        inc1_e2r = round(inc5r - farmercost_2r,0)
        inc1_e3r = round(inc5r - farmercost_3r,0)
        inc1_e4r = round(inc5r - farmercost_4r,0)
        inc1_e5r = round(inc5r - farmercost_5r,0)
        inc1_e6r = round(inc5r - farmercost_6r,0)
        inc1_e7r = round(inc5r - farmercost_7r,0)
        inc1_e8r = round(inc5r - farmercost_8r,0)
        inc1_e9r = round(inc5r - farmercost_9r,0)
        inc1_e10r = round(inc5r - farmercost_10r,0)
        inc1_e11r = round(inc5r - farmercost_11r,0)
        inc1_e12r = round(inc5r - farmercost_12r,0)

        self.participant.vars["inc_er"] = [inc1_e1r, inc1_e2r, inc1_e3r, inc1_e4r, inc1_e5r, inc1_e6r,
                                          inc1_e7r, inc1_e8r, inc1_e9r, inc1_e10r, inc1_e11r, inc1_e12r, ]


        self.participant.vars["diff1r"] = [round((inc1r - inc1_a1r),0), (farmercost_1r) ]
        self.participant.vars["diff2r"] = [round((inc1r - inc1_a2r),0), (farmercost_2r) ]
        self.participant.vars["diff3r"] = [round((inc1r - inc1_a3r),0), (farmercost_3r) ]
        self.participant.vars["diff4r"] = [round((inc1r - inc1_a4r),0), (farmercost_4r) ]
        self.participant.vars["diff5r"] = [round((inc1r - inc1_a5r),0), (farmercost_5r)]
        self.participant.vars["diff6r"] = [round((inc1r - inc1_a6r),0), (farmercost_6r) ]
        self.participant.vars["diff7r"] = [round((inc1r - inc1_a7r),0), (farmercost_7r) ]
        self.participant.vars["diff8r"] = [round((inc1r - inc1_a8r),0), (farmercost_8r) ]
        self.participant.vars["diff9r"] = [round((inc1r - inc1_a9r),0), (farmercost_9r) ]
        self.participant.vars["diff10r"] = [round((inc1r - inc1_a10r),0), (farmercost_10r) ]
        self.participant.vars["diff11r"] = [round((inc1r - inc1_a11r),0), (farmercost_11r) ]
        self.participant.vars["diff12r"] = [round((inc1r - inc1_a12r),0), (farmercost_12r) ]

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HLr(self):
        # *******************************************
        # select random row and random outcome
        # *******************************************
        #
        self.participant.vars['HL_rowr'] = random.randint(1, 12)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_randomr'] = random.randint(1, 12)

        self.participant.vars['HL_scenarior'] = random.randint(1,100)

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices_rs1 = [self.rHL_1,
                      self.rHL_2,
                      self.rHL_3,
                      self.rHL_4,
                      self.rHL_5,
                      self.rHL_6,
                      self.rHL_7,
                      self.rHL_8,
                      self.rHL_9,
                      self.rHL_10,
                      self.rHL_11, self.rHL_12]

        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_rs1'] = choices_rs1[self.participant.vars['HL_rowr'] - 1]


        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_scenarior'] <= 30:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_rs1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_HLr'] = self.participant.vars['inc_ar'][self.participant.vars['HL_rowr']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = self.participant.vars["inc1r"]
        elif self.participant.vars['HL_scenarior'] > 30 and self.participant.vars['HL_scenarior'] <= 54:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HLr'] = self.participant.vars['inc_br'][self.participant.vars['HL_rowr']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = self.participant.vars["inc2r"]
        elif self.participant.vars['HL_scenarior'] > 54 and self.participant.vars['HL_scenarior'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HLr'] = self.participant.vars['inc_cr'][self.participant.vars['HL_rowr']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = self.participant.vars["inc3r"]
        elif self.participant.vars['HL_scenarior'] > 73 and self.participant.vars['HL_scenarior'] <= 88:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HLr'] = self.participant.vars['inc_dr'][self.participant.vars['HL_rowr']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = self.participant.vars["inc4r"]
        elif self.participant.vars['HL_scenarior'] > 88 and self.participant.vars['HL_scenarior'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_rs1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HLr'] = self.participant.vars['inc_er'][self.participant.vars['HL_rowr']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HLr'] = self.participant.vars["inc5r"]


        self.payoff = self.participant.vars['payoff_HLr']
        # write the payoff to player.payoff



