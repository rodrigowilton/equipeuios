from django.db import models


class AppBanco(models.Model):
	nome = models.CharField(max_length=50, null=False, blank=False)
	celular = models.CharField(max_length=15, null=False, blank=False)
	cep = models.CharField(max_length=9,null=False, blank=False)
	endereco = models.CharField(max_length=50, null=False, blank=False)
	complemento = models.CharField(max_length=50, null=True, blank=True)
	bairro = models.CharField(max_length=50, null=False, blank=False)
	localidade = models.CharField(max_length=50, null=False, blank=False)
	uf = models.CharField(max_length=2, null=False, blank=False)
	numero = models.CharField(max_length=10, null=False, blank=False)
	datacadastro = models.DateTimeField(auto_now_add=True, null=False, blank=False)
	aceita_whatsapp = models.BooleanField(default=False)


	def __str__(self):
		return self.nome