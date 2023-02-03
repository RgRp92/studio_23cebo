from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Ruggiero Rippo'


import random

class Constants(BaseConstants):
    name_in_url = 'Fase2SF'
    players_per_group = None
    num_rounds = 1

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


class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    quiz = models.CharField(choices=[['1', '20444 €'], ['2', '16361 €'], ['2', '21436 €']],
                            widget=widgets.RadioSelectHorizontal,
                            label='In base alla figura mostrata, quale sarà il suo guadagno se la variazione sarà tra +1% e +10%?',
                            default="")

    quiz2 = models.CharField(choices=[['1', '20444 €'], ['2', '16361 €'], ['2', '21436 €']],
                             widget=widgets.RadioSelectHorizontal,
                             label='In base alla figura mostrata quale sarà il suo guadagno se la variazione sarà tra +1% e +10%?',
                             default="")


    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_2 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_3 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_4 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_5 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_6 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_7 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_8 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_9 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_10 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_11 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)
    HL_12 = models.IntegerField(choices=[[1, 'A'], [2, 'B']], widget=widgets.RadioSelectHorizontal, initial=0)


    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insprem = self.participant.vars['insprem']
        avginc = self.participant.vars['avginc']

        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        disctot = (insvaluedisc + inspremdisc)

        isttot_1 = round((Constants.ist[0] + inspremist + insvalueist),0)
        isttot_2 = round((Constants.ist[1] + inspremist + insvalueist),0)
        isttot_3 = round((Constants.ist[2] + inspremist + insvalueist),0)
        isttot_4 = round((Constants.ist[3] + inspremist + insvalueist),0)
        isttot_5 = round((Constants.ist[4] + inspremist + insvalueist),0)
        isttot_6 = round((Constants.ist[5] + inspremist + insvalueist),0)
        isttot_7 = round((Constants.ist[6] + inspremist + insvalueist),0)
        isttot_8 = round((Constants.ist[7] + inspremist + insvalueist),0)
        isttot_9 = round((Constants.ist[8] + inspremist + insvalueist),0)
        isttot_10 = round((Constants.ist[9] + inspremist + insvalueist),0)
        isttot_11 = round((Constants.ist[10] + inspremist + insvalueist),0)
        isttot_12 = round((Constants.ist[11] + inspremist + insvalueist),0)

        farmercost_1 = round((isttot_1 - disctot),0)
        farmercost_2 = round((isttot_2 - disctot),0)
        farmercost_3 = round((isttot_3 - disctot),0)
        farmercost_4 = round((isttot_4 - disctot),0)
        farmercost_5 = round((isttot_5 - disctot),0)
        farmercost_6 = round((isttot_6 - disctot),0)
        farmercost_7 = round((isttot_7 - disctot),0)
        farmercost_8 = round((isttot_8 - disctot),0)
        farmercost_9 = round((isttot_9 - disctot),0)
        farmercost_10 = round((isttot_10 - disctot),0)
        farmercost_11 = round((isttot_11 - disctot),0)
        farmercost_12 = round((isttot_12 - disctot),0)

        self.participant.vars["farmercost"] = [farmercost_1,farmercost_2,farmercost_3,farmercost_4,farmercost_5,
                                                farmercost_6,farmercost_7,farmercost_8,farmercost_9,farmercost_10,
                                                farmercost_11,farmercost_12]

        inc1 = round(avginc + (-0.25 * avginc),0)
        loss = avginc - inc1
        reimb = 0.7 * loss

        inc2 = round(avginc + (-0.15 * avginc),0)
        inc3 = round(avginc + (-0.05 * avginc),0)
        inc4 = round(avginc + (0.05 * avginc),0)
        inc5 = round(avginc + (0.15 * avginc),0)

        self.participant.vars["inc1"] = inc1
        self.participant.vars["inc2"] = inc2
        self.participant.vars["inc3"] = inc3
        self.participant.vars["inc4"] = inc4
        self.participant.vars["inc5"] = inc5

        inc1_a1 = round(inc1 + reimb - farmercost_1,0)
        inc1_a2 = round(inc1 + reimb - farmercost_2,0)
        inc1_a3 = round(inc1 + reimb - farmercost_3,0)
        inc1_a4 = round(inc1 + reimb - farmercost_4,0)
        inc1_a5 = round(inc1 + reimb - farmercost_5,0)
        inc1_a6 = round(inc1 + reimb - farmercost_6,0)
        inc1_a7 = round(inc1 + reimb - farmercost_7,0)
        inc1_a8 = round(inc1 + reimb - farmercost_8,0)
        inc1_a9 = round(inc1 + reimb - farmercost_9,0)
        inc1_a10 = round(inc1 + reimb - farmercost_10,0)
        inc1_a11 = round(inc1 + reimb - farmercost_11,0)
        inc1_a12 = round(inc1 + reimb - farmercost_12,0)

        self.participant.vars["inc_a"] = [inc1_a1,inc1_a2,inc1_a3,inc1_a4,inc1_a5,inc1_a6,
                                          inc1_a7,inc1_a8,inc1_a9,inc1_a10,inc1_a11,inc1_a12,]

        inc1_b1 = round(inc2 - farmercost_1,0)
        inc1_b2 = round(inc2 - farmercost_2,0)
        inc1_b3 = round(inc2 - farmercost_3,0)
        inc1_b4 = round(inc2 - farmercost_4,0)
        inc1_b5 = round(inc2 - farmercost_5,0)
        inc1_b6 = round(inc2 - farmercost_6,0)
        inc1_b7 = round(inc2 - farmercost_7,0)
        inc1_b8 = round(inc2 - farmercost_8,0)
        inc1_b9 = round(inc2 - farmercost_9,0)
        inc1_b10 = round(inc2 - farmercost_10,0)
        inc1_b11 = round(inc2 - farmercost_11,0)
        inc1_b12 = round(inc2 - farmercost_12,0)

        self.participant.vars["inc_b"] = [inc1_b1, inc1_b2, inc1_b3, inc1_b4, inc1_b5, inc1_b6,
                                          inc1_b7, inc1_b8, inc1_b9, inc1_b10, inc1_b11, inc1_b12, ]

        inc1_c1 = round(inc3 - farmercost_1,0)
        inc1_c2 = round(inc3 - farmercost_2,0)
        inc1_c3 = round(inc3 - farmercost_3,0)
        inc1_c4 = round(inc3 - farmercost_4,0)
        inc1_c5 = round(inc3 - farmercost_5,0)
        inc1_c6 = round(inc3 - farmercost_6,0)
        inc1_c7 = round(inc3 - farmercost_7,0)
        inc1_c8 = round(inc3 - farmercost_8,0)
        inc1_c9 = round(inc3 - farmercost_9,0)
        inc1_c10 = round(inc3 - farmercost_10,0)
        inc1_c11 = round(inc3 - farmercost_11,0)
        inc1_c12 = round(inc3 - farmercost_12,0)

        self.participant.vars["inc_c"] = [inc1_c1, inc1_c2, inc1_c3, inc1_c4, inc1_c5, inc1_c6,
                                          inc1_c7, inc1_c8, inc1_c9, inc1_c10, inc1_c11, inc1_c12, ]

        inc1_d1 = round(inc4 - farmercost_1,0)
        inc1_d2 = round(inc4 - farmercost_2,0)
        inc1_d3 = round(inc4 - farmercost_3,0)
        inc1_d4 = round(inc4 - farmercost_4,0)
        inc1_d5 = round(inc4 - farmercost_5,0)
        inc1_d6 = round(inc4 - farmercost_6,0)
        inc1_d7 = round(inc4 - farmercost_7,0)
        inc1_d8 = round(inc4 - farmercost_8,0)
        inc1_d9 = round(inc4 - farmercost_9,0)
        inc1_d10 = round(inc4 - farmercost_10,0)
        inc1_d11 = round(inc4 - farmercost_11,0)
        inc1_d12 = round(inc4 - farmercost_2,0)

        self.participant.vars["inc_d"] = [inc1_d1, inc1_d2, inc1_d3, inc1_d4, inc1_d5, inc1_d6,
                                          inc1_d7, inc1_d8, inc1_d9, inc1_d10, inc1_d11, inc1_d12, ]

        inc1_e1 = round(inc5 - farmercost_1,0)
        inc1_e2 = round(inc5 - farmercost_2,0)
        inc1_e3 = round(inc5 - farmercost_3,0)
        inc1_e4 = round(inc5 - farmercost_4,0)
        inc1_e5 = round(inc5 - farmercost_5,0)
        inc1_e6 = round(inc5 - farmercost_6,0)
        inc1_e7 = round(inc5 - farmercost_7,0)
        inc1_e8 = round(inc5 - farmercost_8,0)
        inc1_e9 = round(inc5 - farmercost_9,0)
        inc1_e10 = round(inc5 - farmercost_10,0)
        inc1_e11 = round(inc5 - farmercost_11,0)
        inc1_e12 = round(inc5 - farmercost_12,0)

        self.participant.vars["inc_e"] = [inc1_e1, inc1_e2, inc1_e3, inc1_e4, inc1_e5, inc1_e6,
                                          inc1_e7, inc1_e8, inc1_e9, inc1_e10, inc1_e11, inc1_e12, ]


        self.participant.vars["diff1"] = [round((inc1 - inc1_a1),0), (farmercost_1) ]
        self.participant.vars["diff2"] = [round((inc1 - inc1_a2),0), (farmercost_2) ]
        self.participant.vars["diff3"] = [round((inc1 - inc1_a3),0), (farmercost_3) ]
        self.participant.vars["diff4"] = [round((inc1 - inc1_a4),0), (farmercost_4) ]
        self.participant.vars["diff5"] = [round((inc1 - inc1_a5),0), (farmercost_5)]
        self.participant.vars["diff6"] = [round((inc1 - inc1_a6),0), (farmercost_6) ]
        self.participant.vars["diff7"] = [round((inc1 - inc1_a7),0), (farmercost_7) ]
        self.participant.vars["diff8"] = [round((inc1 - inc1_a8),0), (farmercost_8) ]
        self.participant.vars["diff9"] = [round((inc1 - inc1_a9),0), (farmercost_9) ]
        self.participant.vars["diff10"] = [round((inc1 - inc1_a10),0), (farmercost_10) ]
        self.participant.vars["diff11"] = [round((inc1 - inc1_a11),0), (farmercost_11) ]
        self.participant.vars["diff12"] = [round((inc1 - inc1_a12),0), (farmercost_12) ]

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        # *******************************************
        # select random row and random outcome
        # *******************************************
        #
        self.participant.vars['HL_row'] = random.randint(1, 12)

        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1, 12)

        self.participant.vars['HL_scenario'] = random.randint(1,100)

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices_s1 = [self.HL_1,
                      self.HL_2,
                      self.HL_3,
                      self.HL_4,
                      self.HL_5,
                      self.HL_6,
                      self.HL_7,
                      self.HL_8,
                      self.HL_9,
                      self.HL_10,
                      self.HL_11, self.HL_12]

        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice_s1'] = choices_s1[self.participant.vars['HL_row'] - 1]


        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_scenario'] <= 30:
            # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice_s1'] == 1: #A
                # if the choice was A
                self.participant.vars['payoff_HL'] = self.participant.vars['inc_a'][self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = self.participant.vars["inc1"]
        elif self.participant.vars['HL_scenario'] > 30 and self.participant.vars['HL_scenario'] <= 54:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = self.participant.vars['inc_b'][self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = self.participant.vars["inc2"]
        elif self.participant.vars['HL_scenario'] > 54 and self.participant.vars['HL_scenario'] <= 73:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = self.participant.vars['inc_c'][self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = self.participant.vars["inc3"]
        elif self.participant.vars['HL_scenario'] > 73 and self.participant.vars['HL_scenario'] <= 88:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = self.participant.vars['inc_d'][self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = self.participant.vars["inc4"]
        elif self.participant.vars['HL_scenario'] > 88 and self.participant.vars['HL_scenario'] <= 100:
            # if the random number is larger than the random row
            if self.participant.vars['HL_choice_s1'] == 1 :#A
                    # if the choice was A
                self.participant.vars['payoff_HL'] = self.participant.vars['inc_e'][self.participant.vars['HL_row']-1]
                    # because HL_row is the same as p in the MPL
            else:
                self.participant.vars['payoff_HL'] = self.participant.vars["inc5"]


        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff

