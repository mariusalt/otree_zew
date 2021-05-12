from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

class Constants(BaseConstants):
    name_in_url = 'refgame'
    players_per_group = 4
    endowment = c(100)
    alpha = 4.4  # parameter for benefits from private account
    beta = 0.02  # parameter for benefits from private account
    gamma = 1  # parameter for benefits from public account
    tau = 100  # parameter to calibrate payoff
    instructions_template = 'refgame/instr_content.html'
    payofftable_template = 'refgame/table_content.html'
    chat_template = 'refgame/papercups.html'
    rounds_phase = 2  # Runden pro Phase
    num_phase = 2  # Anzahl an Phasen
    num_rounds = rounds_phase*num_phase


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    avg_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    avg_payoff = models.CurrencyField()


class Player(BasePlayer):
    # Control Questions
    total_payoff = models.CurrencyField()
    pay_round = models.IntegerField()
    wrong = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q1 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q2 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q3 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q4 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q5 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q6 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)

    cq_1 = models.IntegerField(  # control question 1 (cq_1)
        min=0)

    cq_2 = models.IntegerField(  # control question 2 (cq_2)
        min=0)

    cq_3 = models.IntegerField(  # control question 3 (cq_3)
        choices=[5, 10, 15, 20],
        widget=widgets.RadioSelect()
    )

    cq_4 = models.IntegerField(  # control question 4 (cq_4)
        choices=[
            [1, "ja"],
            [2, "nein"],
        ], widget=widgets.RadioSelect()
    )

    cq_5 = models.IntegerField(  # control question 5 (cq_5)
        choices=[0, 50, 70, 90, 100],
        widget=widgets.RadioSelect()
    )

    cq_6 = models.IntegerField(  # control question 6 (cq_6)
        choices=[
            [1, "Aus den 5x5=25 Runden wird eine Runde ausgelost und ausgezahlt."],
            [2, "Eine der fünf Phasen, die aus fünf Runden bestehen, wird ausgelost und ausgezahlt"],
            [3, "Alle 5x5=25 Runden werden ausgezahlt"],
        ], widget=widgets.RadioSelect()
    )

    # Contribution
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment, label="",
    )

    # Cumulative payoff
    cum_payoff = models.CurrencyField()

    # Avg. contribution other group members
    avg_contribution_others = models.CurrencyField()

    # Questions
    q_1_1 = models.IntegerField( # post-question 1: age
        min=0)
    q_1_2 = models.IntegerField( # post-question 2: gender
        choices=[
            [1, "Divers"],
            [2, "Weiblich"],
            [3, "Männlich"],
            [4, "Keine Antwort"]
        ], widget=widgets.RadioSelect()
    )
    q_1_3 = models.IntegerField( # post-question 3: mother tongue
        choices=[
            [1, "Ja"],
            [2, "Nein"],
            [3, "Keine Antwort"]
        ], widget=widgets.RadioSelect()
    )
    q_1_4 = models.IntegerField( # post-question 4: income
        choices=[
            [1, "bis unter 500 Euro"],
            [2, "500 bis 1.000 Euro"],
            [3, "bis unter 1.500 Euro"],
            [4, "1.500 bis unter 2.000 Euro"],
            [5, "2.000 bis unter 2.500 Euro"],
            [6, "2.500 bis unter 3.000 Euro"],
            [7, "3.000 bis unter 3.500 Euro"],
            [8, "über 3.500 Euro"],
            [9, "Keine Antwort"]
        ]
    )


    q_2_1 = models.IntegerField( # post-question XX: risk
        choices=[
            [1, "0: gar nicht risikobereit"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10: sehr risikobereit"],
        ]
    )

    q_2_2 = models.IntegerField(  # post-question XX: trust
        choices=[
            [1, "0: Man kann nicht vorsichtig genug sein"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10: Man kann den meisten vertrauen"],
        ]
    )

    q_2_3 = models.IntegerField(  # post-question XX: exploitation
        choices=[
            [1, "0: Die Menschen nutzen einen aus"],
            [2, "1"],
            [3, "2"],
            [4, "3"],
            [5, "4"],
            [6, "5"],
            [7, "6"],
            [8, "7"],
            [9, "8"],
            [10, "9"],
            [11, "10: Die Menschen verhalten sich fair"],
        ]
    )


    q_3_1= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 0% Chance auf 30 EURO, 100% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_2= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 5% Chance auf 30 EURO, 95% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_3= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 10% Chance auf 30 EURO, 90% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_4= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 15% Chance auf 30 EURO, 85% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_5= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 20% Chance auf 30 EURO, 80% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_6= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 25% Chance auf 30 EURO, 75% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_7= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 30% Chance auf 30 EURO, 70% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_8= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 35% Chance auf 30 EURO, 65% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_9= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 40% Chance auf 30 EURO, 60% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_10= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 45% Chance auf 30 EURO, 55% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_11= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 50% Chance auf 30 EURO, 50% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_12= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 55% Chance auf 30 EURO, 45% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_13= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 60% Chance auf 30 EURO, 40% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_14= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 65% Chance auf 30 EURO, 35% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_15= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 70% Chance auf 30 EURO, 30% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )

    q_3_16= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 75% Chance auf 30 EURO, 25% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )
    q_3_17= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 80% Chance auf 30 EURO, 20% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )
    q_3_18= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 85% Chance auf 30 EURO, 15% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )
    q_3_19= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 90% Chance auf 30 EURO, 10% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )
    q_3_20= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 95% Chance auf 30 EURO, 5% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )
    q_3_21= models.IntegerField( # post-question 3_1
        choices=[
            [1, "Lotterie: 100% Chance auf 30 EURO, 0% Chance auf 16 EURO"],
            [2, "sichere Auszahlung: 20 EURO "],
        ], widget=widgets.RadioSelectHorizontal
    )


    
    betr = models.IntegerField()

    taxi = models.IntegerField(  
        choices=[
            [1, "Taxiunternehmen A"],
            [2, "Taxiunternehmen B"],
        ], widget=widgets.RadioSelectHorizontal
    )


    q_1_5 = models.IntegerField(  # post-question 5: FuS
    min=0, max = 20)

    q_1_6 = models.IntegerField(  # post-question 6: FuS
    min=0, max = 20)






################# FUNCTIONS

# Payoff function
    

def set_payoffs(group):
    players = group.get_players()
    contributions = [p.contribution for p in players]
    group.total_contribution = sum(contributions)
    group.avg_contribution = sum(contributions) / Constants.players_per_group
    for p in players:  # avg. contributions of other group members
        p.avg_contribution_others = (group.total_contribution - p.contribution) / (Constants.players_per_group - 1)
    # group.avg_contribution = (group.total_contribution / Constants.players_per_group)
    # group.individual_share = (    # template payoff for linear public goods game
    #        group.total_contribution / Constants.players_per_group
    #)
    # for p in players:
    #    p.payoff = Constants.endowment - p.contribution + group.individual_share
    for p in players:  # payoff
        p.payoff = Constants.alpha * (Constants.endowment - p.contribution) - \
                   Constants.beta * (Constants.endowment - p.contribution) ** 2 \
                   + Constants.gamma * group.total_contribution - \
                   Constants.tau
    for p in players:  # cumulative payoff
        
        #bestimme nach jeder Runde den bisherigen kumulativen payoff in dieser Phase (Phase geht von p.round_number-p.participant.phase_count+1 bis p.round_number)
        p.cum_payoff = sum([p.payoff for p in p.in_rounds(p.round_number-p.participant.phase_count+1,p.round_number)])
    group.avg_payoff = sum([p.payoff for p in players]) / Constants.players_per_group
    for p in players:
        if p.round_number % Constants.rounds_phase == 0:
            # Wenn das noch nicht die letzte Runde ist, aber die letzte Runde dieser Phase, dann nehme den bisherigen kumilierten payoff 
            # und speicher ihn in der Liste participant.pay_phases
            if p.round_number!=Constants.num_rounds:
                p.participant.pay_phases.append(p.cum_payoff)
                # Setze für die kommende Phase die Variable, die die Anzahl der Runden in dieser Phase zählt, wieder auf Null
                p.participant.phase=p.participant.phase+1
            else:
                p.participant.pay_phases.append(p.cum_payoff)
                # Falls dies die allerletzte Runde ist, bestimme eine Zufallsvariable zwischen 1 und num_phase, um zu bestimmen welche Runde auszahlungsrelevant wird
                p.pay_round=random.choice(range(Constants.num_phase-1))+1
                # Nimm diese Zufallsvariable und bestimme die jeweilige kummulierte Auszahlung aus der gewissen Runde anhand der Liste, in der wir das gespeichert haben (participant.pay_phases)
                p.total_payoff = p.participant.pay_phases[p.pay_round-1]



# Error messages
def cq_1_error_message(player, value):  # error message cq_1
    if value != 294:
        if player.wrong_Q1==0:
            player.wrong_Q1=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q1=+1
            return '<b>Die korrekte Antwort ist 294</b>. Bitte nutzen Sie die <b>Payoff-Tabelle</b> oder den ' \
                   '<b>Payoff-Simulator</b> im Help Desk, um die Berechnung nachzuvollziehen.'



def cq_2_error_message(player, value):  # error message cq_2
    if value != 164:
        if player.wrong_Q2==0:
            player.wrong_Q2=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q2=+1
            return '<b>Die korrekte Antwort ist 164</b>. Bitte nutzen Sie die <b>Payoff-Tabelle</b> oder den ' \
                   '<b>Payoff-Simulator</b> im Help Desk, um die Berechnung nachzuvollziehen.'


def cq_3_error_message(player, value):  # error message cq_3
    if value != 15:
        if player.wrong_Q3==0:
            player.wrong_Q3=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q3=+1
            return '<b>Die korrekte Antwort ist 15 mit einer Auszahlung in Höhe von 189.5</b>. Bitte nutzen Sie die ' \
                   '<b>Payoff-Tabelle</b> oder den <b>Payoff-Simulator</b> im Help Desk, um die Berechnung ' \
                   'nachzuvollziehen.'


def cq_4_error_message(player, value):  # error message cq_4
    if value != 2:
        if player.wrong_Q4==0:
            player.wrong_Q4=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q4=+1
            return 'Selbst wenn die anderen nichts beitragen, ist es besser einen positiven Beitrag zu leisten ' \
               '(beste Antwort ist immer 15). Bitte nutzen Sie die <b>Payoff-Tabelle</b> oder den' \
               ' <b>Payoff-Simulator</b> im Help Desk, um die Berechnung nachzuvollziehen.'


def cq_5_error_message(player, value):  # error message cq_5
    if value != 90:
        if player.wrong_Q5==0:
            player.wrong_Q5=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q5=+1
            return '<b>Die korrekte Antwort ist 90 mit einer Auszahlung in Höhe von 302</b>. Bitte nutzen Sie die ' \
                   '<b>Payoff-Tabelle</b> oder den <b>Payoff-Simulator</b> im Help Desk, ' \
                   'um die Berechnung nachzuvollziehen.'


def cq_6_error_message(player, value):  # error message cq_6
    if value != 2:
        if player.wrong_Q6==0:
            player.wrong_Q6=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q6=+1
            return 'Bitte beachten Sie, dass eine der fünf Phasen ausgelost und ausgezahlt wird.'



################ PAGES

class Willkommen(Page):  # welcome page
    form_model = 'player'

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.phase_count=1
        player.participant.pay_phases=[]
        player.participant.phase=1

    def is_displayed(player):  # welcome only once
        return player.round_number == 1


class Instruktionen(Page):  # Instructions
    form_model = "player"

    def is_displayed(player):  # instructions only once
        return player.round_number == 1


# Kontrollfragen
class Kontrollfragen(Page):  # Control questions
    form_model = "player"
    form_fields = ["wrong","cq_1", "cq_2", "cq_3", "cq_4", "cq_5", "cq_6"]

    def is_displayed(player):  # control questions only once
        return player.round_number == 1

class NeuePhase(Page):
    def is_displayed(player):  # only once
        if player.round_number==1: 
            return True
        elif (player.round_number+1) % Constants.rounds_phase == 0:
            return True
        else:
            return False


class Beitragsentscheidung(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def is_displayed(player):
        return player.round_number <= Constants.num_rounds


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    def is_displayed(player):
        return player.round_number <= Constants.num_rounds


class Results(Page):
    @staticmethod
    def vars_for_template(player):
        dicci1={}
        for k,i in enumerate(range(player.round_number-player.participant.phase_count,player.round_number)):
            nam="contriallR"+str(k+1)
            dicci1[nam]=(player.in_round(i+1).group.get_player_by_id(1).contribution+player.in_round(i+1).group.get_player_by_id(2).contribution+player.in_round(i+1).group.get_player_by_id(3).contribution+player.in_round(i+1).group.get_player_by_id(4).contribution)/4
            nam="payallR"+str(k+1)
            dicci1[nam]=(player.in_round(i+1).group.get_player_by_id(1).payoff+player.in_round(i+1).group.get_player_by_id(2).payoff+player.in_round(i+1).group.get_player_by_id(3).payoff+player.in_round(i+1).group.get_player_by_id(4).payoff)/4
            for p in range(4):
                nam="contriP"+str(p+1)+"R"+str(k+1)
                dicci1[nam]= player.in_round(i+1).group.get_player_by_id(p+1).contribution
                nam="payP"+str(p+1)+"R"+str(k+1)
                dicci1[nam]= player.in_round(i+1).group.get_player_by_id(p+1).payoff
        return dicci1
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.round_number % Constants.rounds_phase == 0:
            player.participant.phase_count=1
        else:
            player.participant.phase_count=player.participant.phase_count+1


class FinalResults(Page):
    @staticmethod
    def vars_for_template(player):
        dicci={}
        for k,i in enumerate(player.participant.pay_phases):
            nam="pay_phase"+str(k+1)
            exec("global %s; %s = i" % (nam,nam))
            dicci[nam]= i
        return dicci
            
        
    def is_displayed(player):  # only once
        return player.round_number == Constants.num_rounds



class Questionnaire(Page):  # welcome page
    form_model = 'player'
    form_fields = ["q_1_1", "q_1_2", "q_1_3", "q_1_4",
                   "q_2_1", "q_3_1", "q_3_2", "q_3_3", "q_3_4", "q_3_5", "q_3_6", "q_3_7", "q_3_8", "q_3_9", "q_3_10",
                    "q_3_11", "q_3_12", "q_3_13", "q_3_14", "q_3_15", "q_3_16", "q_3_17", "q_3_18", "q_3_19", "q_3_20", "q_3_21",
                     "q_2_2", "q_2_3",
                   "betr","taxi", "q_1_5", "q_1_6"]
    @staticmethod
    def vars_for_template(player):
        return dict( 
                fields1 = ["q_3_1", "q_3_2", "q_3_3", "q_3_4", "q_3_5", "q_3_6", "q_3_7", "q_3_8", "q_3_9", "q_3_10",
                    "q_3_11", "q_3_12", "q_3_13", "q_3_14", "q_3_15", "q_3_16", "q_3_17", "q_3_18", "q_3_19", "q_3_20", "q_3_21"], 
              ) 

    def is_displayed(player):  # only once
        return player.round_number == Constants.num_rounds

page_sequence = [Willkommen,
                 Instruktionen,
                 Kontrollfragen,
                 NeuePhase,
                 Beitragsentscheidung,
                 ResultsWaitPage,
                 Results,
                 FinalResults,
                 Questionnaire]
