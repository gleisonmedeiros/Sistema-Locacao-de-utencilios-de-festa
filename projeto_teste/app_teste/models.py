from django.db import models

# Create your models here.

class Produto_Model(models.Model):
    nome = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} - {self.modelo}'


class Cliente_Model(models.Model):
    nome = models.CharField(max_length=80)
    telefone = models.CharField(max_length=80)
    cep = models.CharField(max_length=10)
    estado = models.CharField(max_length=20)
    cidade = models.CharField(max_length=60)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    referencia = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Pedido_Model(models.Model):
    cliente = models.ForeignKey(Cliente_Model, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto_Model)
    data_locacao = models.CharField(max_length=10, blank=True, null=True)
    observacoes = models.TextField(blank=True)




