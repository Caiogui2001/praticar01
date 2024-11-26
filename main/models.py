from django.db import models

class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)  
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} - {self.cpf}'
