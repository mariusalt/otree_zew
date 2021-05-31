from otree.api import Currency as c, currency_range
from . import *
from otree.api import Bot
import random
import itertools
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)



class PlayerBot(Bot):
	def play_round(self):
		if self.round_number == 1:
			yield	(Willkommen)
			yield	(Instruktionen)
			if Constants.treatment == "vcm":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,wrong=1),check_html=False)
			elif Constants.treatment == "wRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=20,cq_8=20,wrong=1),check_html=False)
			elif Constants.treatment == "sRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=21,cq_8=24,wrong=1),check_html=False)
			elif Constants.treatment == "minwRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=20,cq_8=20,wrong=1),check_html=False)
			elif Constants.treatment == "minsRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=21,cq_8=24,wrong=1),check_html=False)
			elif Constants.treatment == "nbminsRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=21,cq_8=24,wrong=1),check_html=False)
			elif Constants.treatment == "nbminsRat":
				yield	Submission(Kontrollfragen, dict(cq_1=294,cq_2=164,cq_3=15,cq_4=2,cq_5=90,cq_6=2,cq_7=21,cq_8=24,wrong=1),check_html=False)

		if Constants.treatment == "minwRat" or Constants.treatment == "minsRat" or Constants.treatment == "nbminwRat" or Constants.treatment == "nbminsRat":
			if (self.round_number-3) % Constants.rounds_phase == 0 or self.round_number==1:
				yield   Submission(MinCon, dict(mincon=random.randrange(0,101,1)),check_html=False)
				yield	(MinConRes)

		if self.round_number==1 or (self.round_number-3) % Constants.rounds_phase == 0:
			yield	(NeuePhase)

		if Constants.treatment == "vcm":
			yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(0,101,1)),check_html=False)
		elif Constants.treatment == "wRat" or Constants.treatment == "nbminwRat":
			if self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(self.player.in_round(self.round_number-1).contribution,101,1)),check_html=False)
			else:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(0,101,1)),check_html=False)
		elif Constants.treatment == "sRat" or Constants.treatment == "nbminsRat":
			if self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0 and self.player.in_round(self.round_number-1).contribution < 100:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange((self.player.in_round(self.round_number-1).contribution+1),101,1)),check_html=False)
			elif self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0 and self.player.in_round(self.round_number-1).contribution == 100:
				yield   Submission(Beitragsentscheidung, dict(contribution=100),check_html=False)
			else:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(0,101,1)),check_html=False)
		elif Constants.treatment == "minwRat":
			if self.round_number==1 or (self.round_number-3) % Constants.rounds_phase == 0:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(self.participant.mincon_group,101,1)),check_html=False)
			if self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(self.player.in_round(self.round_number-1).contribution,101,1)),check_html=False)
		elif Constants.treatment == "minsRat":
			if self.round_number==1 or (self.round_number-3) % Constants.rounds_phase == 0:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange(self.participant.mincon_group,101,1)),check_html=False)
			if self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0 and self.player.in_round(self.round_number-1).contribution < 100:
				yield   Submission(Beitragsentscheidung, dict(contribution=random.randrange((self.player.in_round(self.round_number-1).contribution+1),101,1)),check_html=False)
			elif self.round_number>1 and (self.round_number-3) % Constants.rounds_phase != 0 and self.player.in_round(self.round_number-1).contribution == 100:
				yield   Submission(Beitragsentscheidung, dict(contribution=100),check_html=False)

		yield	(Results)

		if self.round_number==Constants.num_rounds:
			yield	(FinalResults)	
			yield Submission(Questionnaire, dict(q_1_1=random.randrange(1,80,1), q_1_2=random.randrange(1,5,1), q_1_3=random.randrange(1,4,1), q_1_4=random.randrange(1,10,1),q_2_1=random.randrange(1,12,1),q_2_2=random.randrange(1,12,1), q_2_3=random.randrange(1,12,1), risk=str(random.randrange(1,101,1)),betr=str(random.randrange(1,101,1)),taxi=random.randrange(1,3,1), q_1_5=random.randrange(1,21,1), q_1_6=random.randrange(1,21,1)),check_html=False)
			yield	(GoodBye)
			yield   (Ende)

