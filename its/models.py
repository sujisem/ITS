from django.db import models

# Create your models here.
"""
class Question(models.Model):
	class Meta:
		db_table = "question"
		managed=False
	id = models.IntegerField(primary_key=True)
	desc = models.CharField(max_length=1000)
	
class Student(models.Model):
	class Meta:
		db_table = "student"
		managed=False
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	level= models.IntegerField()

class Answers(models.Model):
	class Meta:
		db_table = "answers"
		managed=False
	id = models.IntegerField(primary_key=True)
	qnid=models.ForeignKey(Question, db_column="qnid",on_delete=models.CASCADE)
	desc = models.CharField(max_length=1000)
	iscorrect=models.IntegerField()

class Replies(models.Model):
	class Meta:
		db_table = "replies"
		managed=False
		unique_together = ("qnid","ansid", "repid")
	qnid=models.ForeignKey(Question, db_column="qnid",on_delete=models.CASCADE,primary_key=True)
	ansid = models.ForeignKey(Answers, db_column="ansid",on_delete=models.CASCADE,primary_key=True)
	repid=models.IntegerField(primary_key=True)
	desc = models.CharField(max_length=1000)

class Session(models.Model):
	class Meta:
		db_table = "session"
		managed=False
	id = models.IntegerField(primary_key=True)
	start = models.DateTimeField()
	end= models.DateTimeField()

class Stdintxn(models.Model):
	class Meta:
		db_table = "stdintxn"
		managed=False
		unique_together = ("qnid","ansid", "stdid","sessid")
	qnid=models.ForeignKey(Question, db_column="qnid",on_delete=models.CASCADE)
	ansid = models.ForeignKey(Answers, db_column="ansid",on_delete=models.CASCADE)
	stdid = models.ForeignKey(Student, db_column="stdid",on_delete=models.CASCADE)
	sessid = models.ForeignKey(Session, db_column="sessid",on_delete=models.CASCADE)
	stdid=models.IntegerField()
	"""
		


	
	