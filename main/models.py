from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.IntegerField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

