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
    rounds_phase = 5  # Runden pro Phase
    num_phase = 5  # Anzahl an Phasen
    trial_rounds = 2
    num_rounds = rounds_phase*num_phase + trial_rounds
 #   treatment = "vcm" #treatments: "vcm", "wRat","sRat", "minwRat","minsRat","nbminwRat","nbminsRat"



class Subsession(BaseSubsession):
    def creating_session(self):
        players = self.get_players()
        num_group = len(players)/4
        for i in range(num_group):
            new_group = [
                players.pop(),
                players.pop(),
                players.pop(),
                players.pop(),
            ]
            group_matrix.append(new_group)

        self.set_groups(group_matrix)


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    avg_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    avg_payoff = models.CurrencyField()
    #Minimum contribution outcome
    mincon_group = models.CurrencyField()
    pay_round = models.IntegerField()



class Player(BasePlayer):
    # Control Questions
    total_payoff = models.CurrencyField()
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
    wrong_Q7 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q8 = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q9a = models.IntegerField(initial=0,  # num incorrect answers control questions
        min=0)
    wrong_Q9b = models.IntegerField(initial=0,  # num incorrect answers control questions
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
            [2, "Eine der fünf Phasen, die aus fünf Runden bestehen, wird ausgelost und ausgezahlt."],
            [3, "Alle 5x5=25 Runden werden ausgezahlt."],
        ], widget=widgets.RadioSelect()
    )

    cq_7 = models.IntegerField(  # control question 7 (cq_7)
    min=0, max = 100)

    cq_8 = models.IntegerField(  # control question 8 (cq_8)
    min=0, max = 100)

    cq_9a = models.IntegerField(  # control question 9a (cq_9a)
        min=0, max=100
    )

    cq_9b = models.IntegerField(  # control question 9b (cq_9b)
        min=0, max=100
    )

    # Contribution
    contribution = models.IntegerField(#initial=0,############!!!Delete "initial=0" before prodrun
        min=0, max=Constants.endowment, label="",
    )

    #Minimum contribution
    mincon = models.IntegerField(
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
            [5, "über 2.000 Euro"]
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

    
    risk= models.StringField()
    
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

    

    wrsl1 = models.IntegerField(initial=0, blank=True)
    wrsl2 = models.IntegerField(initial=0, blank=True)




################# FUNCTIONS



# Payoff function
def set_mincon(group):
    players = group.get_players()
    all_mincon = [p.mincon for p in players]
    group.mincon_group = min(all_mincon)
    for p in players:
        p.participant.mincon_group=group.mincon_group
    

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
    # Falls dies die allerletzte Runde ist, bestimme eine Zufallsvariable zwischen 1 und num_phase, um zu bestimmen welche Runde auszahlungsrelevant wird
    group.pay_round=random.choice(range(Constants.num_phase-1))+1
    for p in players:
        if (p.round_number-2) % Constants.rounds_phase == 0:
            # Wenn das noch nicht die letzte Runde ist, aber die letzte Runde dieser Phase, dann nehme den bisherigen kumilierten payoff 
            # und speicher ihn in der Liste participant.pay_phases
            if (p.round_number) !=Constants.num_rounds:
                p.participant.pay_phases.append(p.cum_payoff)
            else:
                p.participant.pay_phases.append(p.cum_payoff)
                # Nimm diese Zufallsvariable und bestimme die jeweilige kummulierte Auszahlung aus der gewissen Runde anhand der Liste, in der wir das gespeichert haben (participant.pay_phases)
                p.total_payoff = p.participant.pay_phases[group.pay_round-1]
    



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

def cq_7_error_message(player, value):  # error message cq_6
    if player.session.config['treatment']=="wRat" or player.session.config['treatment']=="minwRat" or player.session.config['treatment']=="nbminwRat":
        if value != 20:
            if player.wrong_Q7==0:
                player.wrong_Q7=+1
                return 'Die Antwort ist leider nicht korrekt.'
            else:
                player.wrong_Q7=+1
                return '<b>Die korrekte Antwort ist 20 LD</b>. Bitte beachten Sie, dass Ihr Beitrag in allen weiteren' \
                       ' Runden mindestens so hoch sein muss, wie in der Runde zuvor.'
    elif player.session.config['treatment']=="sRat" or player.session.config['treatment']=="minsRat" or player.session.config['treatment']=="nbsRat":
        if value != 21:
            if player.wrong_Q7==0:
                player.wrong_Q7=+1
                return 'Die Antwort ist leider nicht korrekt.'
            else:
                player.wrong_Q7=+1
                return 'Bitte beachten Sie, dass Ihr Beitrag höher sein muss, als in der Runde zuvor.'

def cq_8_error_message(player, value):  # error message cq_6
    if player.session.config['treatment']=="wRat" or player.session.config['treatment']=="minwRat"  or player.session.config['treatment']=="nbminwRat":
        if value != 20:
            if player.wrong_Q8==0:
                player.wrong_Q8=+1
                return 'Die Antwort ist leider nicht korrekt.'
            else:
                player.wrong_Q8=+1
                return '<b>Die korrekte Antwort ist 20 LD</b>.Bitte beachten Sie, dass Ihr Beitrag in allen weiteren ' \
                       'Runden mindestens so hoch sein muss, wie in der Runde zuvor.'
    elif player.session.config['treatment']=="sRat" or player.session.config['treatment']=="minsRat" or player.session.config['treatment']=="nbminsRat":
        if value != 24:
            if player.wrong_Q8==0:
                player.wrong_Q8=+1
                return 'Die Antwort ist leider nicht korrekt.'
            else:
                player.wrong_Q8=+1
                return 'Bitte beachten Sie, dass Ihr Beitrag in allen weiteren Runden jewils höher sein muss, ' \
                       'als in der Runde zuvor.'

def cq_9a_error_message(player, value):  # error message cq_1
    if value != 10:
        if player.wrong_Q9a==0:
            player.wrong_Q9a=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q9a=+1
            return '<b>Die korrekte Antwort ist 10</b>. Ihr Beitrag muss mindestens so hoch sein wie das Minimum der ' \
                   'Angaben für den kollektiven Mindestbeitrag.'
def cq_9b_error_message(player, value):  # error message cq_9b
    if value != 0:
        if player.wrong_Q9a==0:
            player.wrong_Q9a=+1
            return 'Die Antwort ist leider nicht korrekt.'
        else:
            player.wrong_Q9a=+1
            return '<b>Die korrekte Antwort ist 0</b>. Inwieweit Sie dem Vorschlag für den kollektiven Mindestbeitrag folgen (hier = 10), können Sie selbst entscheiden.'

def contribution_error_message(player, value):  # error message cq_1
    if player.session.config['treatment']=="wRat"  or player.session.config['treatment']=="nbminwRat":
        if player.round_number>1 and (player.round_number-3) % Constants.rounds_phase != 0:
            if value < player.in_round(player.round_number-1).contribution:
                return 'Sie müssen einen Beitrag wählen, der mindestens so hoch ist, wie Ihr Beitrag aus der vorherigen' \
                       ' Runde. <br>Ihr Beitrag in der vorherigen Runde betrug '\
                       + str(player.in_round(player.round_number-1).contribution) +' LD.'
    if player.session.config['treatment']=="sRat" or player.session.config['treatment']=="nbminsRat":
        if player.round_number>1 and (player.round_number-3) % Constants.rounds_phase != 0 and value < 100:
            if value <= player.in_round(player.round_number-1).contribution:
                return 'Sie müssen einen Beitrag wählen, der höher ist, als Ihr Beitrag aus der vorherigen Runde. ' \
                       '<br>Ihr Beitrag in der vorherigen Runde betrug '\
                       + str(player.in_round(player.round_number-1).contribution) +' LD.'
    if player.session.config['treatment']=="minwRat":
        if player.round_number==1 or (player.round_number-3) % Constants.rounds_phase == 0:
            if value < player.participant.mincon_group:
                return 'Sie müssen einen Beitrag wählen, der mindestens so hoch ist, wie der Mindestbeitrag, welcher bei ' + str(player.participant.mincon_group) +' LD liegt.'
        if player.round_number>1 and (player.round_number-3) % Constants.rounds_phase != 0:
            if value < player.in_round(player.round_number-1).contribution or value < player.participant.mincon_group:
                return 'Sie müssen einen Beitrag wählen, der mindestens so hoch ist, wie Ihr Beitrag aus der vorherigen Runde.<br>Ihr Beitrag in der vorherigen Runde betrug ' + str(player.in_round(player.round_number-1).contribution) +' LD.'
    if player.session.config['treatment']=="minsRat":
        if player.round_number==1 or (player.round_number-3) % Constants.rounds_phase == 0:
            if value < player.participant.mincon_group:
                return 'Sie müssen einen Beitrag wählen, der mindestens so hoch ist, wie der Mindestbeitrag, welcher bei ' + str(player.participant.mincon_group) +' LD liegt.'
        if player.round_number>1 and (player.round_number-3) % Constants.rounds_phase != 0 and value < 100:
            if value <= player.in_round(player.round_number-1).contribution or value < player.participant.mincon_group:
                return 'Sie müssen einen Beitrag wählen, der höher ist, als Ihr Beitrag aus der vorherigen Runde.<br>Ihr Beitrag in der vorherigen Runde betrug ' + str(player.in_round(player.round_number-1).contribution) +' LD.'





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
    form_fields = ["wrong","cq_1", "cq_2", "cq_3", "cq_4", "cq_5", "cq_6", "cq_7", "cq_8", "cq_9a", "cq_9b"]
    def is_displayed(player):  # control questions only once
        return player.round_number == 1

class MinCon(Page):
    form_model = 'player'
    form_fields = ['mincon']

    def is_displayed(player):
        if player.session.config['treatment'] == "minwRat" or player.session.config['treatment'] == "minsRat" or player.session.config['treatment'] == "nbminwRat" or player.session.config['treatment'] == "nbminsRat":
            if (player.round_number-3) % Constants.rounds_phase == 0 or player.round_number == 1:
                return True
            else:
                return False
        else:
            return False

class MinConWaitPage(WaitPage):
    after_all_players_arrive = 'set_mincon'

    def is_displayed(player):
        if player.session.config['treatment'] == "minwRat" or player.session.config['treatment'] == "minsRat" or player.session.config['treatment'] == "nbminwRat" or player.session.config['treatment'] == "nbminsRat":
            if (player.round_number-3) % Constants.rounds_phase == 0 or player.round_number == 1:
                return True
            else:
                return False
        else:
            return False

class MinConRes(Page):
    def is_displayed(player):
        if player.session.config['treatment'] == "minwRat" or player.session.config['treatment'] == "minsRat" or player.session.config['treatment'] == "nbminwRat" or player.session.config['treatment'] == "nbminsRat":
            if (player.round_number-3) % Constants.rounds_phase == 0 or player.round_number == 1:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def vars_for_template(player):
        p1_mc = player.group.get_player_by_id(1).mincon
        p2_mc = player.group.get_player_by_id(2).mincon
        p3_mc = player.group.get_player_by_id(3).mincon
        p4_mc = player.group.get_player_by_id(4).mincon
        return dict(
            p1_mc=p1_mc,
            p2_mc=p2_mc,
            p3_mc=p3_mc,
            p4_mc=p4_mc
        )
    

class NeuePhase(Page):
    def is_displayed(player):  # only once
        if player.round_number==1: 
            return True
        elif (player.round_number-3) % Constants.rounds_phase == 0:
            return True
        else:
            return False


class Beitragsentscheidung(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def is_displayed(player):
        return player.round_number <= Constants.num_rounds

    def vars_for_template(player):
        if player.round_number>1:
            disp_rat = (player.round_number-3) % Constants.rounds_phase != 0
            if player.session.config['treatment'] == "minwRat" or player.session.config['treatment'] == "minsRat":
                if player.in_round(player.round_number-1).contribution >= player.participant.mincon_group:
                    last_con = player.in_round(player.round_number-1).contribution
                    last_con_s = player.in_round(player.round_number-1).contribution+1
                else:
                    last_con = player.participant.mincon_group
                    last_con_s = player.participant.mincon_group
            else:
                last_con = player.in_round(player.round_number-1).contribution
                if player.in_round(player.round_number-1).contribution < 100:
                    last_con_s = player.in_round(player.round_number-1).contribution+1
                else:
                    last_con_s = 100
        else:
            disp_rat = False
            last_con = 0
            last_con_s = 0

        return dict( disp_rat = disp_rat, last_con = last_con, last_con_s = last_con_s)


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
        if (player.round_number-2) % Constants.rounds_phase == 0 :
            player.participant.phase=player.participant.phase+1
        if (player.round_number-2) % Constants.rounds_phase == 0:
            player.participant.phase_count=1
        else:
            player.participant.phase_count=player.participant.phase_count+1

        if player.round_number == Constants.trial_rounds:
            player.payoff==0
            player.participant.phase_count=1
            player.participant.pay_phases=[]
            player.participant.phase=1



class FinalResults(Page):
    @staticmethod
    def vars_for_template(player):
        dicci={}
        for k,i in enumerate(player.participant.pay_phases):
            nam="pay_phase"+str(k+1)
            exec("global %s; %s = i" % (nam,nam))
            dicci[nam]= i
        dicci["payeuro"]= round(player.total_payoff/100,2)
        return dicci
            
        
    def is_displayed(player):  # only once
        return player.round_number == Constants.num_rounds



class Questionnaire(Page):  # welcome page
    form_model = 'player'
    form_fields = ["q_1_1", "q_1_2", "q_1_3", "q_1_4",
                   "q_2_1",
                     "q_2_2", "q_2_3", "risk",
                   "betr","taxi", "q_1_5", "q_1_6","wrsl1","wrsl2"]
    

    def is_displayed(player):  # only once
        return player.round_number == Constants.num_rounds

class GoodBye(Page): # good bye page
    form_model = 'player'

    def is_displayed(player): # only once
        return player.round_number == Constants.num_rounds

class Ende(Page): # good bye page

    def is_displayed(player): # only once
        return player.round_number == Constants.num_rounds

page_sequence = [Willkommen,
                 Instruktionen,
                 Kontrollfragen,
                 NeuePhase,
                 MinCon,
                 MinConWaitPage,
                 MinConRes,
                 Beitragsentscheidung,
                 ResultsWaitPage,
                 Results,
                 FinalResults,
                 Questionnaire,
                 GoodBye,
                 Ende]
