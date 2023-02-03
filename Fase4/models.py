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
    name_in_url = 'Fase4'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.IntegerField(label='1. Anno di nascita', min=1900, max=2012)
    q2 = models.StringField(
        choices=[['0', 'M'], ['1', 'F']],
        label='2. Genere',
        widget=widgets.RadioSelect,
    )
    q3 = models.StringField(
        choices=[['0', 'Scuola elementare'], ['1', 'Diploma scuola superiore'],
                 ['2', 'Laurea 3 anni'], ['3', 'Laurea 5 anni'], ['4', 'Master'],
                 ['5', 'Dottorato']],
        label='3. Titolo di studio',
        widget=widgets.RadioSelect,
    )
    q4 = models.StringField(
        choices=[['0', 'Fino a 5 anni'], ['1', 'Da 5 a 9 anni'],
                 ['2', 'Da 10 a 20 anni'],
                 ['3', 'Più di 20 anni']],
        label='4. Da quanti anni è coinvolto nella coltivazione delle mele?',
        widget=widgets.RadioSelect,
    )

    q5 = models.StringField(
        choices=[['0', 'SI'], ['1', 'NO'],['2','Non saprei']],
        label='5. Pensa che la sua attività melicola sarà continuata nel futuro da un familiare?',
        widget=widgets.RadioSelect)

    q6 = models.StringField(
        choices=[['0', 'Rischi di produzione: grandine, gelate tardive, fitopatie'],
                 ['1', 'Rischi di mercato: variazioni prezzo di vendita delle mele, aumento prezzi dei fattori di produzione (costo fitosanitari, prezzo conicimi, costo carburanti)'],
                 ['2', 'Rischi finanziari:accesso ai mutui, mancanza di riserve finanziarie, debiti insoluti'],
                 ['3', 'Rischi istituzionali: cambio regolamenti imprevisti (es. regolamentazione dei fitosanitari EU)'],
                 ['4', 'Rischi personali: malattia personale, infortuni sul lavoro, problemi familiari']],
        label='6. Quali sono i rischi maggiori che hanno inciso sul reddito aziendale (da mele) negli ultimi 3 anni?',
        widget=widgets.RadioSelect)

    q7_a1 = models.BooleanField(blank=True, initial=False)
    q7_a2 = models.BooleanField(blank=True, initial=False)
    q7_a3 = models.BooleanField(blank=True, initial=False)
    q7_a4 = models.BooleanField(blank=True, initial=False)
    q7_a5 = models.BooleanField(blank=True, initial=False)

    q7_b1 = models.BooleanField(blank=True, initial=False)
    q7_b2 = models.BooleanField(blank=True, initial=False)
    q7_b3 = models.BooleanField(blank=True, initial=False)
    q7_b4 = models.BooleanField(blank=True, initial=False)
    q7_b5 = models.BooleanField(blank=True, initial=False)

    q7_c1 = models.BooleanField(blank=True, initial=False)
    q7_c2 = models.BooleanField(blank=True, initial=False)
    q7_c3 = models.BooleanField(blank=True, initial=False)
    q7_c4 = models.BooleanField(blank=True, initial=False)
    q7_c5 = models.BooleanField(blank=True, initial=False)

    q7_d1 = models.BooleanField(blank=True, initial=False)
    q7_d2 = models.BooleanField(blank=True, initial=False)
    q7_d3 = models.BooleanField(blank=True, initial=False)
    q7_d4 = models.BooleanField(blank=True, initial=False)
    q7_d5 = models.BooleanField(blank=True, initial=False)

    q7_e1 = models.BooleanField(blank=True, initial=False)
    q7_e2 = models.BooleanField(blank=True, initial=False)
    q7_e3 = models.BooleanField(blank=True, initial=False)
    q7_e4 = models.BooleanField(blank=True, initial=False)
    q7_e5 = models.BooleanField(blank=True, initial=False)

    q7_f1 = models.BooleanField(blank=True, initial=False)
    q7_f2 = models.BooleanField(blank=True, initial=False)
    q7_f3 = models.BooleanField(blank=True, initial=False)
    q7_f4 = models.BooleanField(blank=True, initial=False)
    q7_f5 = models.BooleanField(blank=True, initial=False)

    q8_a1 = models.BooleanField(blank=True, initial=False)
    q8_a2 = models.BooleanField(blank=True, initial=False)
    q8_a3 = models.BooleanField(blank=True, initial=False)
    q8_a4 = models.BooleanField(blank=True, initial=False)
    q8_a5 = models.BooleanField(blank=True, initial=False)

    q8_b1 = models.BooleanField(blank=True, initial=False)
    q8_b2 = models.BooleanField(blank=True, initial=False)
    q8_b3 = models.BooleanField(blank=True, initial=False)
    q8_b4 = models.BooleanField(blank=True, initial=False)
    q8_b5 = models.BooleanField(blank=True, initial=False)

    q8_c1 = models.BooleanField(blank=True, initial=False)
    q8_c2 = models.BooleanField(blank=True, initial=False)
    q8_c3 = models.BooleanField(blank=True, initial=False)
    q8_c4 = models.BooleanField(blank=True, initial=False)
    q8_c5 = models.BooleanField(blank=True, initial=False)

    q8_d1 = models.BooleanField(blank=True, initial=False)
    q8_d2 = models.BooleanField(blank=True, initial=False)
    q8_d3 = models.BooleanField(blank=True, initial=False)
    q8_d4 = models.BooleanField(blank=True, initial=False)
    q8_d5 = models.BooleanField(blank=True, initial=False)

    q8_e1 = models.BooleanField(blank=True, initial=False)
    q8_e2 = models.BooleanField(blank=True, initial=False)
    q8_e3 = models.BooleanField(blank=True, initial=False)
    q8_e4 = models.BooleanField(blank=True, initial=False)
    q8_e5 = models.BooleanField(blank=True, initial=False)

    q8_f1 = models.BooleanField(blank=True, initial=False)
    q8_f2 = models.BooleanField(blank=True, initial=False)
    q8_f3 = models.BooleanField(blank=True, initial=False)
    q8_f4 = models.BooleanField(blank=True, initial=False)
    q8_f5 = models.BooleanField(blank=True, initial=False)

    q9 = models.StringField(
        choices=[['0','Variazione prezzi di mercato delle mele'],
                 ['1','Variazione costo carburanti'],
                 ['2','Variazione costo fertilizzanti'],
                 ['3','Variazione costo energia'],
                 ['4','Variazione costo manodopera'],
                 ['5','Variazione costo packaging/imballaggio'],
                 ['6','Variazione costi addebitati cooperativa'],
                 ['7','Variazione costo macchinari'],
                 ['8','Variazione regolamentazioni Europee'],
                 ['9','Altro']],
        label= '9. Quali sono i rischi di mercato che hanno inciso sul reddito aziendale (da mele) negli ultimi 3 anni?',
        widget=widgets.RadioSelect)

    q10 = models.StringField(
        choices=[['0', 'Variazione prezzi di mercato delle mele'],
                 ['1', 'Variazione costo carburanti'],
                 ['2', 'Variazione costo fertilizzanti'],
                 ['3', 'Variazione costo energia'],
                 ['4', 'Variazione costo manodopera'],
                 ['5', 'Variazione costo packaging/imballaggio'],
                 ['6', 'Variazione costi addebitati cooperativa'],
                 ['7', 'Variazione costo macchinari'],
                 ['8', 'Variazione regolamentazioni Europee'],
                 ['9', 'Altro']],
        label='10. Quali sono i rischi di mercato che incideranno maggiormente sul reddito aziendale (da mele) nei prossimi 3 anni?',
        widget=widgets.RadioSelect)

    q11 = models.StringField(
        choices=[['0', 'Variazione costo packaging/imballaggio'],
                 ['1', 'Quantità e qualità produzione estera'],
                 ['2', 'Quantità e qualità produzione da altre regioni italiane'],
                 ['3', 'Variazioni riserve di mele (giacenze)'],
                 ['4', 'Qualità mele prodotte'],
                 ['5', 'Cambiamenteo nella domanda, abitudini alimentari e/o stili di vita dei consumatori']],
        label='11. Quali sono state le cause che hanno inciso maggiormente sul prezzo delle mele negli ultimi 3 anni?',
        widget=widgets.RadioSelect)

    q12 = models.StringField(
        choices=[['0', 'Variazione costo packaging/imballaggio'],
                 ['1', 'Quantità e qualità produzione estera'],
                 ['2', 'Quantità e qualità produzione da altre regioni italiane'],
                 ['3', 'Variazioni riserve di mele (giacenze)'],
                 ['4', 'Qualità mele prodotte'],
                 ['5', 'Cambiamenteo nella domanda, abitudini alimentari e/o stili di vita dei consumatori']],
        label='12. Quali sono le cause che incideranno maggiormente sul prezzo delle mele nei prossimi 3 anni?',
        widget=widgets.RadioSelect )

    q13_a = models.BooleanField(blank=True, initial=False)
    q13_b = models.BooleanField(blank=True, initial=False)
    q13_c = models.BooleanField(blank=True, initial=False)
    q13_d = models.BooleanField(blank=True, initial=False)
    q13_e = models.BooleanField(blank=True, initial=False)

    q14_a = models.BooleanField(blank=True, initial=False)
    q14_b = models.BooleanField(blank=True, initial=False)
    q14_c = models.BooleanField(blank=True, initial=False)
    q14_d = models.BooleanField(blank=True, initial=False)
    q14_e = models.BooleanField(blank=True, initial=False)

    q15_a = models.BooleanField(blank=True, initial=False)
    q15_b = models.BooleanField(blank=True, initial=False)
    q15_c = models.BooleanField(blank=True, initial=False)
    q15_d = models.BooleanField(blank=True, initial=False)
    q15_e = models.BooleanField(blank=True, initial=False)

    q16_a = models.BooleanField(blank=True, initial=False)
    q16_b = models.BooleanField(blank=True, initial=False)
    q16_c = models.BooleanField(blank=True, initial=False)
    q16_d = models.BooleanField(blank=True, initial=False)
    q16_e = models.BooleanField(blank=True, initial=False)
    q16_f = models.BooleanField(blank=True, initial=False)
    q16_g = models.BooleanField(blank=True, initial=False)
    q16_h = models.BooleanField(blank=True, initial=False)
    q16_i = models.BooleanField(blank=True, initial=False)

    q17_a = models.BooleanField(blank=True, initial=False)
    q17_b = models.BooleanField(blank=True, initial=False)
    q17_c = models.BooleanField(blank=True, initial=False)
    q17_d = models.BooleanField(blank=True, initial=False)
    q17_e = models.BooleanField(blank=True, initial=False)
    q17_f = models.BooleanField(blank=True, initial=False)

    q18_a = models.BooleanField(blank=True, initial=False)
    q18_b = models.BooleanField(blank=True, initial=False)
    q18_c = models.BooleanField(blank=True, initial=False)
    q18_d = models.BooleanField(blank=True, initial=False)
    q18_e = models.BooleanField(blank=True, initial=False)
    q18_f = models.BooleanField(blank=True, initial=False)

    check1 = models.BooleanField(blank=True, initial=False)
    check2 = models.BooleanField(blank=True, initial=False)

    q20_a = models.BooleanField(blank=True, initial=False)
    q20_b = models.BooleanField(blank=True, initial=False)
    q20_c = models.BooleanField(blank=True, initial=False)
    q20_d = models.BooleanField(blank=True, initial=False)
    q20_e = models.BooleanField(blank=True, initial=False)
    q20_f = models.BooleanField(blank=True, initial=False)
    q20_g = models.BooleanField(blank=True, initial=False)
    q20_h = models.BooleanField(blank=True, initial=False)
    q20_i = models.BooleanField(blank=True, initial=False)
    q20_j = models.BooleanField(blank=True, initial=False)

    q21_a = models.BooleanField(blank=True, initial=False)
    q21_b = models.BooleanField(blank=True, initial=False)
    q21_c = models.BooleanField(blank=True, initial=False)
    q21_d = models.BooleanField(blank=True, initial=False)
    q21_e = models.BooleanField(blank=True, initial=False)
    q21_f = models.BooleanField(blank=True, initial=False)
    q21_g = models.BooleanField(blank=True, initial=False)
    q21_h = models.BooleanField(blank=True, initial=False)
    q21_i = models.BooleanField(blank=True, initial=False)
    q21_j = models.BooleanField(blank=True, initial=False)

    q22 = models.StringField(
        choices=[['0','Per niente'],
                 ['1','Poco'],
                 ['2','Abbastanza'],
                 ['3', 'Molto']],
        label='21. Quanto è importante per Lei la stabilizzazione del reddito (da mele)?',
        widget=widgets.RadioSelect )

    q23 = models.StringField(
        choices=[['0', 'Per niente'],
                 ['1', 'Poco'],
                 ['2', 'Abbastanza'],
                 ['3', 'Molto']],
        label='22. Pensa che il Fondo IST Mele bbia la capacità di stabilizzare il reddito (da mele)?',
        widget=widgets.RadioSelect)

    q24 = models.StringField(
        choices=[['0','Sicuramente no'],
                 ['1', 'Forse no'],
                 ['2', 'Non lo so'],
                 ['3', 'Forse si'],
                 ['4', 'Sicuramente si']],
        label='23. Pensa di aderire al Fondo IST Mele nel 2023?',
        widget=widgets.RadioSelect)

    qf1 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf4 = models.StringField(
        choices=[['1',''], ['2',''],['3',''],['4',''],['5','']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qf7 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Fiducia',
        widget=widgets.RadioSelectHorizontal,
    )
    qc1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc7 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qc8 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Cooperazione',
        widget=widgets.RadioSelectHorizontal,
    )
    qi1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi5 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi6 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qi7 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Assimetria Informativa',
        widget=widgets.RadioSelectHorizontal,
    )
    qh1 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Azzardo Morale',
        widget=widgets.RadioSelectHorizontal,
    )
    qh2 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Azzardo Morale',
        widget=widgets.RadioSelectHorizontal,
    )
    qh3 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Azzardo Morale',
        widget=widgets.RadioSelectHorizontal,
    )
    qh4 = models.StringField(
        choices=[['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', '']],
        label='Azzardo Morale',
        widget=widgets.RadioSelectHorizontal,
    )


    qmail = models.StringField(
        choices=[['0', 'Si'],
                 ['1','No']],
        label='Vorrebbe che la sua mail venisse inserita in un database ed essere contatto per eventuali studi futuri?',
        widget=widgets.RadioSelect )
