# -*- encoding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import decimal
import math
"""
Copyright (c) 2019 - present AppSeed.us
"""

"""A tabela CadCliente é utilizada para cadastrar novos clientes no sistema
ou seja, sempre que uma pessoa (que esteja no banco de dados cadastrado na tabela Pessoa)
realizar uma venda ela é adicionada na tabela CadCliente"""
class CadCliente(models.Model):
    vendedor = models.ForeignKey('Pessoas', on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(_(""), max_length=128, blank=True, null=True)
    codigo = models.IntegerField(_(""), blank=True, null=True)

    taxas = models.DecimalField(_("Taxas"), max_digits=5, decimal_places=2, blank=True, null=True)
    sim = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    nao = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    operacional = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    tcc = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    honorarios = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    animal = models.CharField(_(""), max_length=256, blank=True, null=True)
    evento = models.CharField(_(""), max_length=256, blank=True, null=True)
    informar_repasse = models.CharField(_(""), max_length=50, blank=True, null=True)
    vl_juros = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    vl_boletos = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    vl_pago = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    deposito = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    repasse = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)


    class Meta:
        verbose_name = _("cad_cliente")
        verbose_name_plural = _("cad_clientes")
        db_table = 'cad_cliente'
        managed = True

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("cad_cliente_model_detail", kwargs={"pk": self.pk})

class Comissao_Vendedor(models.Model):
    #id, default django
    comissao = models.DecimalField(_(""), max_digits=5, decimal_places=2)
    vendedor = models.ForeignKey('Pessoas', on_delete=models.CASCADE, blank=True, null=True)
    taxa_percentual = models.DecimalField(_(""), max_digits=5, decimal_places=2, blank=True, null=True)
    taxa_de_comissao = models.DecimalField(_(""), max_digits=5, decimal_places=2, default=1/100, blank=True, null=True)
    nome = models.CharField(_(""), max_length=128, blank=True, null=True)
    id_contrato = models.ForeignKey('Contratos', on_delete=models.CASCADE, blank=True, null=True)
    numero_contrato = models.IntegerField(_(""), blank=True, null=True)
    codigo_parcela = models.IntegerField(_(""), blank=True, null=True)

    class Meta:
        verbose_name = _("Comissao_Vendedor")
        verbose_name_plural = _("Comissao_Vendedores")
        db_table = 'comissao_vendedor'
        managed = True

    def __str__(self):
        return f'{self.nome}, comissao: {self.comissao}'

    def get_absolute_url(self):
        return reverse("Comissao_Vendedores_detail", kwargs={"pk": self.pk})


    
class Debito(models.Model):
    vl_debito = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True)
    dt_debitado = models.DateField(_(""), blank=True, null=True)
    taxas = models.ForeignKey('Taxa', on_delete=models.DO_NOTHING, blank=True, null=True)
    descricao = models.CharField(_(""), max_length=256, blank=True, null=True)
    
    class Meta:
        verbose_name = _("debito")
        verbose_name_plural = _("debitos")
        db_table = 'debito'

    def __str__(self):
        return f'{self.cliente} - {self.vl_debito}'

    def get_absolute_url(self):
        return reverse("debito_detail", kwargs={"pk": self.pk})


class Credito(models.Model):
    dt_creditado = models.DateField(_(""), blank=True, null=True)
    vl_credito = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    taxas = models.ForeignKey('Taxa', on_delete=models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True)
    descricao = models.CharField(_(""), max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = _("credito")
        verbose_name_plural = _("creditos")
        managed = True
        db_table = 'credito'

    def __str__(self):
        #retorne o id
        return f'{self.cliente.nome} - {self.vl_credito}'

    def get_absolute_url(self):
        return reverse("credito_detail", kwargs={"pk": self.pk})


class Taxa(models.Model):
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True)
    taxas = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(_(""), max_length=128, blank=True, null=True)
    vl_pago = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    descricao = models.CharField(_(""), max_length=256, blank=True, null=True)
    dt_taxa = models.DateField(_(""), blank=True, null=True)
    class Meta:
        verbose_name = _("taxas")
        verbose_name_plural = _("taxas")
        db_table = 'taxas'
        managed = True
        #ordering = ['id']

    def __str__(self):
        return f'{self.cliente.nome or "Sem Nome"}'

    def get_absolute_url(self):
        return reverse("taxas_detail", kwargs={"pk": self.pk})



class Calculo_Repasse(models.Model):
    #id: default django
    #TODO: o id_contrato e o id_vendedor são instancias de Contratos e Pessoas, alterar o nome para vendedor e contrato
    id_vendedor = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True)
    id_contrato = models.ForeignKey('Contratos', on_delete=models.DO_NOTHING, blank=True, null=True)
    contrato_parcelas = models.ForeignKey('ContratoParcelas', on_delete=models.DO_NOTHING, blank=True, null=True)
    deposito = models.CharField(_(""), max_length=128, blank=True, null=True)
    taxas = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    adi = models.CharField(_(""), max_length=12, blank=True, null=True)
    me = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    op = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    banco = models.CharField(_(""), max_length=50, blank=True, null=True)
    #?repasses: veio da planilha
    repasses = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    calculo = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    nu_parcela = models.IntegerField(_(""), blank=True, null=True)
    comissao = models.CharField(_(""), max_length=128, blank=True, null=True)
    dt_credito = models.DateField(_(""),blank=True, null=True)
    #? o vl_pago pode ser encontrado no modelo DadosArquivoRetorno
    vl_pago = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    #?repasse: assim que o modelo é criado e devidamente salvo ele é computado com base nas regras do calculo e salvado
    repasse = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    
    
    """ @property
    def calculo_model(self) -> decimal.Decimal:
        return decimal.Decimal(
            float(self.vl_pago or 0) - float(self.taxas or 0)
        ).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
    
    @property
    def me_model(self) -> decimal.Decimal:
        #arredondar para cima sempre
        if (self.adi in ['Sim', 'sim', 'SIM','S', 's']):
            #return self.calculo_model * 0.2
            return decimal.Decimal(
                float(self.calculo_model) * 0.03
            ).quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_HALF_UP)
        return decimal.Decimal(
            float(self.calculo_model) * 0.2
        ).quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_HALF_UP)
    
    @property
    def repasses_model(self) -> decimal.Decimal:
        return decimal.Decimal(
            float(self.vl_pago or 0) - float(self.taxas or 0) - float(self.me_model)
        ).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_HALF_UP)
    
    #*metodo save
    def save(self, force_insert, using) -> None:
        self.repasse = self.repasses_model
        self.me = self.me_model
        self.calculo = self.calculo_model
        return super().save(force_insert=force_insert, using=using) """
    
    class Meta:
        verbose_name = _("calculo_repasse")
        verbose_name_plural = _("calculo_repasses")
        #*o nome Calculo_Repasse deveria estar como: 'calculo_repasse'
        db_table = 'Calculo_Repasse'
        managed = True

    def __str__(self):
        return f'repasses: {self.repasses}'

    def get_absolute_url(self):
        return reverse("calculo_repasse_detail", kwargs={"pk": self.pk})
    
""" esse modelo serve para puxar todos os dados que estão na planilha
e facilitar a consulta caso haja erro de dados no Calculo_Repasse"""
class Dado(models.Model):
    id_vendedor = models.IntegerField(_(""), blank=True, null=True)
    id_contrato = models.IntegerField(_(""), blank=True, null=True)
    vendedor = models.CharField(_(""), max_length=100, blank=True, null=True)
    comprador = models.CharField(_(""), max_length=100, blank=True, null=True)
    nu_parcela = models.CharField(_(""), max_length=100, blank=True, null=True)
    contrato = models.IntegerField(_(""), blank=True, null=True)
    vl_pago = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    dt_vencimento = models.DateField(_(""),blank=True, null=True)
    dt_credito = models.DateField(_(""),blank=True, null=True)
    banco = models.CharField(_(""), max_length=50, blank=True, null=True)
    evento = models.CharField(_(""), max_length=512, blank=True, null=True)
    deposito = models.CharField(_(""), max_length=50, blank=True, null=True)
    calculo = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    taxas = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    adi = models.CharField(_(""), max_length=12, blank=True, null=True)
    me = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    op = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    repasses = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    comissao = models.CharField(_(""), max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = _("Dado")
        verbose_name_plural = _("Dados")

    def __str__(self):
        return f'{self.id_contrato}, {self.vendedor}'

    def get_absolute_url(self):
        return reverse("Dado_detail", kwargs={"pk": self.pk})


class Quinzenal(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = 'quinzenal'
        managed = True
        verbose_name = 'Quinzenal'
        verbose_name_plural = 'Quinzenais'