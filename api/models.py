from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
   
    def __str__(self):
        return self.cidade
    
    class Meta:
        db_table = 'cliente'
    

class Cidade(models.Model):
    cidade = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cidade

    class Meta:
        db_table = 'cidade'


