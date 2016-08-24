from django.db import models

# Create your models here.
class Dreamreal(models.Model):
    website = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "dreamreal"

# political party model
class PoliticalParty(models.Model):
    website = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "political_party"

class Voter(models.Model):
    name = models.CharField(max_length=50)
    party = models.ForeignKey(PoliticalParty)

    class Meta:
        db_table = "voters"

class Online(models.Model):
    domain = models.CharField(max_length=30)

    class Meta:
        db_table = "online"