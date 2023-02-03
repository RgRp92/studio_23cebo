from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Page0(Page):
    def is_displayed(self):
        return self.round_number == 1

class ISTPage1(Page):
    form_model = 'player'

class ISTPage2(Page):
    form_model = 'player'

class ISTPage3(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = (150 + inspremist + insvalueist)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }
class ISTPage3a(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = (150 + inspremist + insvalueist)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }

class ISTPage3b(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = round((150 + inspremist + insvalueist),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }

class ISTPage3c(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = round((150 + inspremist + insvalueist),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }
class ISTPage3d(Page):
    form_model = 'player'

    def vars_for_template(self):
        applearea = self.participant.vars['applearea']
        appleareaist = self.participant.vars['appleareaist']

        insvalue = self.participant.vars['insvalue']
        insvalueist = round((insvalue * 0.005),2)
        insvaluedisc = round((insvalue * 0.001),2)

        insprem = self.participant.vars['insprem']
        inspremist = round((insprem * 0.04),2)
        inspremdisc = round((insprem * 0.04),2)

        istct = round((150 + inspremist + insvalueist),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct *70)/30),2)

        totfin = (istct + eutot)
        totfin = round(totfin,2)

        return{
            'applearea': applearea,
            'appleareaist': appleareaist,
            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc':inspremdisc,
            'insvaluedisc':insvaluedisc,
            'istct':istct,
            'disctot': disctot,
            'farmercost':farmercost,
            'eutot' : eutot,
            'totfin': totfin,

        }

class ISTPage4(Page):
    form_model = 'player'

    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        insprem = self.participant.vars['insprem']
        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        istct = round((inspremist + insvalueist + 150),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct * 70) / 30), 2)

        totfin = round((istct + eutot),2)

        avginc = self.participant.vars['avginc']
        red = 25
        inc_fut = round(avginc - ((red/100)*avginc),2)
        loss = round(inc_fut - avginc,2)

        ind = round(-(70*loss)/100,2)
        fin_inc = round(inc_fut - farmercost + ind,2)

        return {

            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc': inspremdisc,
            'insvaluedisc': insvaluedisc,
            'istct': istct,
            'disctot': disctot,
            'farmercost': farmercost,
            'eutot': eutot,
            'totfin': totfin,
            'avginc':avginc,
            'red':red,
            'inc_fut':inc_fut,
            'loss': loss,
            'ind': ind,
            'fin_inc': fin_inc

        }

class ISTPage4a(Page):
    form_model = 'player'

    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        insprem = self.participant.vars['insprem']
        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        istct = round((inspremist + insvalueist + 150),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct * 70) / 30), 2)

        totfin = (istct + eutot)

        avginc = self.participant.vars['avginc']
        red = 25
        inc_fut = round(avginc - ((red/100)*avginc),2)
        loss = round(inc_fut - avginc,2)

        ind = round(-(70*loss)/100,2)
        fin_inc = round(inc_fut - farmercost + ind,2)

        return {

            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc': inspremdisc,
            'insvaluedisc': insvaluedisc,
            'istct': istct,
            'disctot': disctot,
            'farmercost': farmercost,
            'eutot': eutot,
            'totfin': totfin,
            'avginc':avginc,
            'red':red,
            'inc_fut':inc_fut,
            'loss': loss,
            'ind': ind,
            'fin_inc': fin_inc

        }
class ISTPage4b(Page):
    form_model = 'player'

    def vars_for_template(self):
        insvalue = self.participant.vars['insvalue']
        insvalueist = (insvalue * 0.005)
        insvaluedisc = (insvalue * 0.001)

        insprem = self.participant.vars['insprem']
        inspremist = (insprem * 0.04)
        inspremdisc = (insprem * 0.04)

        istct = round((inspremist + insvalueist + 150),2)

        disctot = round((insvaluedisc + inspremdisc),2)

        farmercost = round((istct - disctot),2)

        eutot = round(((istct * 70) / 30), 2)

        totfin = (istct + eutot)

        avginc = self.participant.vars['avginc']
        red = 25
        inc_fut = round(avginc - ((red/100)*avginc),2)
        loss = round(inc_fut - avginc,2)

        ind = round(-(70*loss)/100,2)
        fin_inc = round(inc_fut - farmercost + ind,2)

        return {

            'insvalue': insvalue,
            'insvalueist': insvalueist,
            'insprem': insprem,
            'inspremist': inspremist,
            'inspremdisc': inspremdisc,
            'insvaluedisc': insvaluedisc,
            'istct': istct,
            'disctot': disctot,
            'farmercost': farmercost,
            'eutot': eutot,
            'totfin': totfin,
            'avginc':avginc,
            'red':red,
            'inc_fut':inc_fut,
            'loss': loss,
            'ind': ind,
            'fin_inc': fin_inc

        }

class IstruzioniPage1(Page):
    form_model = 'player'

class IstruzioniPage2(Page):
    form_model = 'player'

    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6
        }
class IstruzioniPage2b(Page):
    form_model = 'player'

    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6
        }
class IstruzioniPage2c(Page):
    form_model = 'player'

    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        self.player.vars_for_template()
        rate = round(25000 / self.participant.vars['inc5'], 2)
        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6,
            'rate': rate
        }
class IstruzioniPage2d(Page):
    form_model = 'player'

    def vars_for_template(self):
        var1 = Constants.var1*100
        var2 = Constants.var2*100
        var3 = Constants.var3*100
        var4 = Constants.var4 * 100
        var5 = Constants.var5 * 100
        var6 = Constants.var6 * 100
        self.player.vars_for_template()
        rate = round(25000 / self.participant.vars['inc5'], 2)
        return {
            'var1': var1,
            'var2': var2,
            'var3': var3,
            'var4': var4,
            'var5': var5,
            'var6': var6,
            'rate': rate
        }

class IstruzioniPage3(Page):
    form_model = 'player'
class IstruzioniPage3a(Page):
        form_model = 'player'
class IstruzioniPage3b(Page):
    form_model = 'player'
class IstruzioniPage3c(Page):
    form_model = 'player'

class IstruzioniPage4(Page):
    form_model = 'player'

class IstruzioniPage5(Page):
# which forms are needed from class player
    form_model = 'player'
class IstruzioniPage6(Page):
# which forms are needed from class player
    form_model = 'player'
class IstruzioniPage7(Page):
# which forms are needed from class player
    form_model = 'player'
class IstruzioniPage8(Page):
# which forms are needed from class player
    form_model = 'player'

class EsempioPage1(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'a4': Constants.s1_a1_4,
            'aa4': Constants.s1_a2_4,
        }

class EsempioPage2(Page):
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return {
            'b11': Constants.s1_b1,
            'b12': Constants.s1_b2,
        }

class Esperti(Page):
    form_model = 'player'
class Espertia(Page):
    form_model = 'player'

class Espertib(Page):
    form_model = 'player'
class Espertic(Page):
    form_model = 'player'

class Quiz1(Page):
    form_model = 'player'
    form_fields = ['quiz']

    def vars_for_template(self):
        self.player.vars_for_template()

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

        return {
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

    def before_next_page(self):
        self.participant.vars['quiz'] = self.player.quiz

class Quiz1Right(Page):
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

        return {
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

    def is_displayed(self):
       return self.participant.vars["quiz"] == '1'

class Quiz2(Page):
    form_model = 'player'
    form_fields = ['quiz2']

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

        return {
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

    def is_displayed(self):
       return self.participant.vars["quiz"] != '1'

    def before_next_page(self):
        self.participant.vars["quiz2"] = self.player.quiz2

class Quiz2Right(Page):
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

        return {
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


    def is_displayed(self):
       return self.participant.vars["quiz"] !='1' and self.participant.vars["quiz2"] == '1'

class Quiz2bis(Page):
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

        return {
            'var1': var1,
            'var11': var11,
            'var2': var2,
            'var22': var22,
            'var3': var3,
            'var33': var33,
            'var4': var4,
            'var44': var44,
            'var5': var5,
            'var55': var55
        }


    def is_displayed(self):
       return self.participant.vars["quiz"] !='1' and self.participant.vars["quiz2"] != '1'

class MyWaitPage(Page):
    form_model = 'player'
    def vars_for_template(self):
        self.player.vars_for_template()
        rate = round(25000/self.participant.vars['inc5'],2)
        return {'rate':rate}

    def before_next_page(self):
        self.participant.vars['rate'] = round(25000/self.participant.vars['inc5'],2)

class HL_Page1(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1',
                   'HL_2',
                   'HL_3',
                   'HL_4',
                   'HL_5',
                   'HL_6',
                   'HL_7',
                   'HL_8',
                   'HL_9',
                   'HL_10',
                   'HL_11',
                   'HL_12',
                   ] # all 12 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        self.player.vars_for_template()
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

        return {
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

            'ist1': self.participant.vars["farmercost"][0],
            'ist2': self.participant.vars["farmercost"][1],
            'ist3': self.participant.vars["farmercost"][2],
            'ist4': self.participant.vars["farmercost"][3],
            'ist5': self.participant.vars["farmercost"][4],
            'ist6': self.participant.vars["farmercost"][5],
            'ist7': self.participant.vars["farmercost"][6],
            'ist8': self.participant.vars["farmercost"][7],
            'ist9': self.participant.vars["farmercost"][8],
            'ist10': self.participant.vars["farmercost"][9],
            'ist11': self.participant.vars["farmercost"][10],
            'ist12': self.participant.vars["farmercost"][11],

            'a' : self.participant.vars['inc1'],
            'a_1': self.participant.vars['inc_a'][0],
            'a_2': self.participant.vars['inc_a'][1],
            'a_3': self.participant.vars['inc_a'][2],
            'a_4': self.participant.vars['inc_a'][3],
            'a_5': self.participant.vars['inc_a'][4],
            'a_6': self.participant.vars['inc_a'][5],
            'a_7': self.participant.vars['inc_a'][6],
            'a_8': self.participant.vars['inc_a'][7],
            'a_9': self.participant.vars['inc_a'][8],
            'a_10': self.participant.vars['inc_a'][9],
            'a_11': self.participant.vars['inc_a'][10],
            'a_12': self.participant.vars['inc_a'][11],

            'b': self.participant.vars['inc2'],
            'b_1': self.participant.vars['inc_b'][0],
            'b_2': self.participant.vars['inc_b'][1],
            'b_3': self.participant.vars['inc_b'][2],
            'b_4': self.participant.vars['inc_b'][3],
            'b_5': self.participant.vars['inc_b'][4],
            'b_6': self.participant.vars['inc_b'][5],
            'b_7': self.participant.vars['inc_b'][6],
            'b_8': self.participant.vars['inc_b'][7],
            'b_9': self.participant.vars['inc_b'][8],
            'b_10': self.participant.vars['inc_b'][9],
            'b_11': self.participant.vars['inc_b'][10],
            'b_12': self.participant.vars['inc_b'][11],

            'c': self.participant.vars['inc3'],
            'c_1': self.participant.vars['inc_c'][0],
            'c_2': self.participant.vars['inc_c'][1],
            'c_3': self.participant.vars['inc_c'][2],
            'c_4': self.participant.vars['inc_c'][3],
            'c_5': self.participant.vars['inc_c'][4],
            'c_6': self.participant.vars['inc_c'][5],
            'c_7': self.participant.vars['inc_c'][6],
            'c_8': self.participant.vars['inc_c'][7],
            'c_9': self.participant.vars['inc_c'][8],
            'c_10': self.participant.vars['inc_c'][9],
            'c_11': self.participant.vars['inc_c'][10],
            'c_12': self.participant.vars['inc_c'][11],

            'd': self.participant.vars['inc4'],
            'd_1': self.participant.vars['inc_d'][0],
            'd_2': self.participant.vars['inc_d'][1],
            'd_3': self.participant.vars['inc_d'][2],
            'd_4': self.participant.vars['inc_d'][3],
            'd_5': self.participant.vars['inc_d'][4],
            'd_6': self.participant.vars['inc_d'][5],
            'd_7': self.participant.vars['inc_d'][6],
            'd_8': self.participant.vars['inc_d'][7],
            'd_9': self.participant.vars['inc_d'][8],
            'd_10': self.participant.vars['inc_d'][9],
            'd_11': self.participant.vars['inc_d'][10],
            'd_12': self.participant.vars['inc_d'][11],

            'e': self.participant.vars['inc5'],
            'e_1': self.participant.vars['inc_e'][0],
            'e_2': self.participant.vars['inc_e'][1],
            'e_3': self.participant.vars['inc_e'][2],
            'e_4': self.participant.vars['inc_e'][3],
            'e_5': self.participant.vars['inc_e'][4],
            'e_6': self.participant.vars['inc_e'][5],
            'e_7': self.participant.vars['inc_e'][6],
            'e_8': self.participant.vars['inc_e'][7],
            'e_9': self.participant.vars['inc_e'][8],
            'e_10': self.participant.vars['inc_e'][9],
            'e_11': self.participant.vars['inc_e'][10],
            'e_12': self.participant.vars['inc_e'][11],

            'diff_a1': (-1 * self.participant.vars["diff1"][0]),
            'diff_b1': self.participant.vars["diff1"][1],
            'diff_a2': (-1 * self.participant.vars["diff2"][0]),
            'diff_b2': self.participant.vars["diff2"][1],
            'diff_a3': (-1 * self.participant.vars["diff3"][0]),
            'diff_b3': self.participant.vars["diff3"][1],
            'diff_a4': (-1 * self.participant.vars["diff4"][0]),
            'diff_b4': self.participant.vars["diff4"][1],
            'diff_a5': (-1 * self.participant.vars["diff5"][0]),
            'diff_b5': self.participant.vars["diff5"][1],
            'diff_a6': (-1 * self.participant.vars["diff6"][0]),
            'diff_b6': self.participant.vars["diff6"][1],
            'diff_a7': (-1 * self.participant.vars["diff7"][0]),
            'diff_b7': self.participant.vars["diff7"][1],
            'diff_a8': (-1 * self.participant.vars["diff8"][0]),
            'diff_b8': self.participant.vars["diff8"][1],
            'diff_a9': (-1 * self.participant.vars["diff9"][0]),
            'diff_b9': self.participant.vars["diff9"][1],
            'diff_a10': (-1 * self.participant.vars["diff10"][0]),
            'diff_b10': self.participant.vars["diff10"][1],
            'diff_a11': (-1 * self.participant.vars["diff11"][0]),
            'diff_b11': self.participant.vars["diff11"][1],
            'diff_a12': (-1 * self.participant.vars["diff12"][0]),
            'diff_b12': self.participant.vars["diff12"][1],


        }

    def before_next_page(self):
        self.player.set_payoff_HL()  # see in models in Player class
        self.participant.vars['a1_value'] = self.participant.vars['inc_a'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['a2_value'] = self.participant.vars['inc_b'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['a3_value'] = self.participant.vars['inc_c'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['a4_value'] = self.participant.vars['inc_d'][self.participant.vars['HL_row'] - 1]
        self.participant.vars['a5_value'] = self.participant.vars['inc_e'][self.participant.vars['HL_row'] - 1]

        self.participant.vars['b1_value'] = self.participant.vars['inc1']
        self.participant.vars['b2_value'] = self.participant.vars['inc2']
        self.participant.vars['b3_value'] = self.participant.vars['inc3']
        self.participant.vars['b4_value'] = self.participant.vars['inc4']
        self.participant.vars['b5_value'] = self.participant.vars['inc5']

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

class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
            # retrieve values from participant.vars and store them in a dictionary
            return{
            'payoff_HL': self.player.participant.vars['payoff_HL'],#payoff
            'row': self.player.participant.vars['HL_row'], # randomly chosen row
            'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
            'value2': self.participant.vars['HL_scenario'],
            'choice': self.participant.vars['HL_choice_s1'],# actual choice
            # outcomes of the selected row
            'a1_value': self.participant.vars['inc_a'][self.participant.vars['HL_row'] - 1],
            'a2_value': self.participant.vars['inc_b'][self.participant.vars['HL_row'] - 1],
            'a3_value': self.participant.vars['inc_c'][self.participant.vars['HL_row'] - 1],
            'a4_value': self.participant.vars['inc_d'][self.participant.vars['HL_row'] - 1],
            'a5_value': self.participant.vars['inc_e'][self.participant.vars['HL_row'] - 1],

            'b1_value': self.participant.vars['inc1'],
            'b2_value': self.participant.vars['inc2'],
            'b3_value': self.participant.vars['inc3'],
            'b4_value': self.participant.vars['inc4'],
            'b5_value': self.participant.vars['inc5'],

            'p_A_1': self.participant.vars['HL_row'],
            'p_A_2': 10-self.participant.vars['HL_row'],
            'p_B_1': self.participant.vars['HL_row'],
            'p_B_2': 10-self.participant.vars['HL_row'],
            'ist_value':self.participant.vars["farmercost"][self.participant.vars['HL_row'] - 1],
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
        self.participant.vars['ist_value'] = Constants.ist[self.participant.vars['HL_row'] - 1]




# the coreography of pages
page_sequence = [
    Page0,
    ISTPage1,
    ISTPage2,
    ISTPage3,
    ISTPage3a,
    ISTPage3b,
    ISTPage3c,
    ISTPage3d,
    ISTPage4,
    ISTPage4a,
    ISTPage4b,
    IstruzioniPage1,
    IstruzioniPage2,
    IstruzioniPage2b,
    IstruzioniPage2c,
    IstruzioniPage2d,
    IstruzioniPage3,
    IstruzioniPage3a,
    IstruzioniPage3b,
    IstruzioniPage3c,
    IstruzioniPage6,
    IstruzioniPage7,
    IstruzioniPage8,
    IstruzioniPage4,
    IstruzioniPage5,
    Quiz1,
    Quiz1Right,
    Quiz2,
    Quiz2Right,
    Quiz2bis,
    Esperti,
    Espertia,
    Espertib,
    Espertic,
    MyWaitPage,
    HL_Page1,
    OutcomeHL
]
