# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models
class Answers(models.Model):
    qnid = models.ForeignKey('Question', models.DO_NOTHING, db_column='Qnid')                           # Field name made lowercase.
    id = models.BigIntegerField(db_column='Id', primary_key=True)                                       # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=1000)                                          # Field name made lowercase.
    iscorrect = models.IntegerField(db_column='IsCorrect')                                              # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'answers'
        unique_together = (('id', 'qnid'),)

class Question(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=1000)  # Field name made lowercase.
    difflevel = models.CharField(db_column='Difflevel', max_length=15, blank=True, null=True)  # Field name made lowercase.
    diffnum = models.BigIntegerField(db_column='Diffnum', blank=True, null=True)  # Field name made lowercase.
    topic = models.CharField(db_column='Topic', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question'


class Replies(models.Model):
    qnid = models.ForeignKey(Question, models.DO_NOTHING, db_column='Qnid', primary_key=True)  # Field name made lowercase.
    ansid = models.ForeignKey(Answers, models.DO_NOTHING, db_column='Ansid')  # Field name made lowercase.
    repid = models.BigIntegerField(db_column='Repid')  # Field name made lowercase.
    desc = models.CharField(db_column='Desc', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'replies'
        unique_together = (('qnid', 'ansid', 'repid'),)


class Session(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=50)  # Field name made lowercase.
    start = models.DateTimeField(db_column='Start')  # Field name made lowercase.
    end = models.DateTimeField(db_column='End')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'session'

class Student(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    level = models.IntegerField(db_column='Level')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'

class Stdintxn(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)
    stdid = models.ForeignKey(Student, models.DO_NOTHING, db_column='stdid')  # Field name made lowercase.
    qnid = models.ForeignKey(Question, models.DO_NOTHING, db_column='qnid')  # Field name made lowercase.
    ansid = models.ForeignKey(Answers, models.DO_NOTHING, db_column='ansid')  # Field name made lowercase.
    sessid = models.ForeignKey(Session, models.DO_NOTHING, db_column='sessid')  # Field name made lowercase.
    attempt = models.IntegerField(db_column='attempt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stdintxn'
        unique_together = (('stdid', 'qnid', 'ansid', 'sessid'),)
