from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)

class Cidade(models.Model):
    cidade = models.CharField(max_length=255)


