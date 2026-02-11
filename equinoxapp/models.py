from django.db import models


class Record(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
            return self.nom


class Step(models.Model):
    id = models.IntegerField(primary_key=True)
    target = models.CharField(max_length=300)
    command = models.CharField(max_length=50)
    value = models.CharField(max_length=200)
    record = models.ForeignKey(Record)

    def __str__(self):
            return self.command
