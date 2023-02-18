from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Page0(Page):
    def is_displayed(self):
        return self.round_number == 1

class Page1Demographics(Page):
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5']

class Page2AgriAct(Page):
        form_model = 'player'
        form_fields = ['q6_a1','q6_a2','q6_a3','q6_a4','q6_a5',
                       'q7_a1', 'q7_b1', 'q7_c1','q7_d1','q7_e1','q7_f1',
                       'q7_a2', 'q7_b2', 'q7_c2', 'q7_d2', 'q7_e2', 'q7_f2',
                       'q7_a3', 'q7_b3', 'q7_c3', 'q7_d3', 'q7_e3', 'q7_f3',
                       'q8_a1', 'q8_b1', 'q8_c1', 'q8_d1', 'q8_e1', 'q8_f1',
                       'q8_a2', 'q8_b2', 'q8_c2', 'q8_d2', 'q8_e2', 'q8_f2',
                       'q8_a3', 'q8_b3', 'q8_c3', 'q8_d3', 'q8_e3', 'q8_f3',]
class Page2AgriAct1(Page):
    form_model = 'player'
    form_fields = ['q9_1', 'q9_2', 'q9_3', 'q9_4', 'q9_5', 'q9_6',
                   'q9_7', 'q9_8', 'q9_10',
                   'q10_1', 'q10_2', 'q10_3', 'q10_4', 'q10_5', 'q10_6',
                   'q10_7', 'q10_8', 'q10_10',
                   ]
class Page2AgriAct1A(Page):
    form_model = 'player'
    form_fields = ['q11_1', 'q11_2', 'q11_3', 'q11_4', 'q11_5', 'q11_6',
                   'q12_1', 'q12_2', 'q12_3', 'q12_4', 'q12_5', 'q12_6',
                   ]

class Page3AgriAct2(Page):
    form_model = 'player'
    form_fields = ['q13_a','q13_b','q13_c','q13_d','q13_e',
                   'q14_a','q14_b','q14_c','q14_d','q14_e',
                   'q15_a','q15_b','q15_c','q15_d','q15_e',]

class Page3AgriAct3(Page):
    form_model = 'player'
    form_fields = ['q16_a','q16_b','q16_c','q16_d','q16_e','q16_f','q16_g','q16_h','q16_i',
                   'q17_a','q17_b','q17_c','q17_d','q17_e','q17_f']

class Page4ISTsurvey(Page):
    form_model = 'player'
    form_fields = ['q18_a','q18_b','q18_c','q18_d','q18_e','q18_f',
                   'check1','check2',
                   'q20_a','q20_b','q20_c','q20_d','q20_e','q20_f','q20_g','q20_h','q20_i','q20_j',
                   'q21_a','q21_b','q21_c','q21_d','q21_e','q21_f','q21_g','q21_h','q21_i', 'q21_j',
                   'q22','q23','q24']

class Page5LikertScaleQ(Page):
    form_model = 'player'
    form_fields = ['qf1','qf2','qf3','qf4','qf5','qf6','qf7',
        'qc1','qc2','qc3','qc4','qc5','qc6','qc7']

class Page6LikertScaleQ1(Page):
    form_model = 'player'
    form_fields = ['qi1','qi2','qi3','qi4','qi5','qi6','qi7',
        'qh1','qh2','qh3','qh4']

class ResultsWaitPage(WaitPage):
    pass
class Page7(Page):
    form_model = 'player'
    form_fields = ['qmail']

class Results(Page):
    form_model = 'player'
    form_fields = ['qmail']

page_sequence = [
                 Page1Demographics,
                 Page2AgriAct,
                 Page2AgriAct1,
                 Page2AgriAct1A,
                 Page3AgriAct2,
                 Page3AgriAct3,
                 Page4ISTsurvey,
                 Page5LikertScaleQ,
                 Page6LikertScaleQ1,
                 Page7,
                 Results]
