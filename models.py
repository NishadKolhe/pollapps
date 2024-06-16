from django.db import models

class PollModel(models.Model):
	poll_id = models.IntegerField(primary_key=True)
	question = models.TextField()
	op1 = models.CharField(max_length=40)
	op2 = models.CharField(max_length=40)
	op3 = models.CharField(max_length=40)
	cop1 = models.IntegerField(default=0)
	cop2 = models.IntegerField(default=0)
	cop3 = models.IntegerField(default=0)

	def __str__(self):
		return str(self.question)