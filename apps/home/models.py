# -*- encoding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Sum
import decimal
import math
from . import existing_models
from auditlog.registry import auditlog
#from .existing_models import Pessoas

"""
Copyright (c) 2019 - present AppSeed.us
"""

"""A tabela CadCliente é utilizada para cadastrar novos clientes no sistema
ou seja, sempre que uma pessoa (que esteja no banco de dados cadastrado na tabela Pessoa)
realizar uma venda ela é adicionada na tabela CadCliente"""

class CadCliente(models.Model):
    vendedor = models.ForeignKey('Pessoas', on_delete=models.CASCADE, null=True, related_name='cliente')
    codigo = models.IntegerField(blank=True, null=True)

    taxas = models.DecimalField("Taxas", max_digits=5, decimal_places=2, blank=True, null=True)
    sim = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nao = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    operacional = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tcc = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    honorarios = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    animal = models.CharField(max_length=256, blank=True, null=True)
    evento = models.CharField(max_length=256, blank=True, null=True)
    informar_repasse = models.CharField(max_length=50, blank=True, null=True)
    repasse_semanal = models.BooleanField(default=False, blank=True, null=True)


    class Meta:
        verbose_name = _("cad_cliente")
        verbose_name_plural = _("cad_clientes")
        db_table = 'cad_cliente'
        managed = True

    def __str__(self):
        return f'{self.vendedor or "SEM NOME"}'



class RepasseRetido(models.Model):
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='repasses_retidos')
    vlr_rep_retido = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    dt_rep_retido = models.DateField(_(""), blank=True, null=True)
    tipo = models.CharField(_(""), max_length=128, blank=True, null=True)
    aprovada = models.BooleanField(_("O campo aprovada é utilizado para saber se sera computado para a tabela repasses ou não"), default=False, blank=True, null=True)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)
    
    class Meta:
        verbose_name = _("RepasseRetido")
        verbose_name_plural = _("RepasseRetidos")
        db_table = 'repasse_retido'
        managed = True

    def __str__(self):
        return f'{self.cliente} - {self.vlr_rep_retido}'

    def get_absolute_url(self):
        return reverse("RepasseRetido_detail", kwargs={"pk": self.pk})

    
class Debito(models.Model):
    vl_debito = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='debitos')
    dt_debitado = models.DateField(_(""), blank=True, null=True)
    #taxas = models.ForeignKey('Taxa', on_delete=models.DO_NOTHING, blank=True, null=True)
    descricao = models.CharField(_(""), max_length=256, blank=True, null=True)
    aprovada = models.BooleanField(_(""), default=False, blank=True, null=True)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)
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
    #taxas = models.ForeignKey('Taxa', on_delete=models.DO_NOTHING, blank=True, null=True)
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='creditos')
    descricao = models.CharField(_(""), max_length=128, blank=True, null=True)
    aprovada = models.BooleanField(_(""), default=False, blank=True, null=True)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)

    class Meta:
        verbose_name = _("credito")
        verbose_name_plural = _("creditos")
        managed = True 
        db_table = 'credito'#s

    def __str__(self):
        #retorne o id
        return f'{self.cliente} - {self.vl_credito}'

    def get_absolute_url(self):
        return reverse("credito_detail", kwargs={"pk": self.pk})


class Taxa(models.Model):
    cliente = models.ForeignKey('Pessoas', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='taxas')
    taxas = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(_(""), max_length=128, blank=True, null=True)
    vl_pago = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    descricao = models.CharField(_(""), max_length=256, blank=True, null=True)
    dt_taxa = models.DateField(_(""), blank=True, null=True)
    aprovada = models.BooleanField(_(""), default=False, blank=True, null=True)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)
    
    class Meta:
        verbose_name = _("taxas")
        verbose_name_plural = _("taxas")
        db_table = 'taxas'
        managed = True
        #ordering = ['id']

    def __str__(self):
        return f"{self.taxas}"

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
    id_vendedor = models.CharField(_(""), max_length=128, blank=True, null=True)
    id_contrato = models.CharField(_(""), max_length=128, blank=True, null=True)
    id_comprador = models.CharField(_(""), max_length=128, blank=True, null=True)
    vendedor = models.CharField(_(""), max_length=100, blank=True, null=True)
    comprador = models.CharField(_(""), max_length=100, blank=True, null=True)
    nu_parcela = models.CharField(_(""), max_length=100, blank=True, null=True)
    parcelas_contrato = models.CharField(_(""), max_length=50, blank=True, null=True)
    vl_pago = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    dt_vencimento = models.DateField(_(""),blank=True, null=True)
    dt_credito = models.DateField(_(""),blank=True, null=True)
    banco = models.CharField(_(""), max_length=50, blank=True, null=True)
    contrato = models.TextField(_(""), blank=True, null=True)
    evento = models.TextField(_(""), blank=True, null=True)
    deposito = models.CharField(_(""), max_length=300, blank=True, null=True)
    calculo = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    taxas = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    adi = models.CharField(_(""), max_length=12, blank=True, null=True)
    me = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    op = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    repasses = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    comissao = models.CharField(_(""), max_length=128, blank=True, null=True)
    id_excel = models.IntegerField(_(""), blank=True, null=True)
    #!abaixo estão os campos para identificar quais são os dados aprovados
    repasse_aprovado = models.BooleanField(_("Essa opção serve para identificar se determinado dado foi aprovado para repasse"),
                                           default=False, blank=True, null=True)
    criado = models.DateTimeField(_(""), auto_now_add=True, blank=True, null=True)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Dado")
        verbose_name_plural = _("Dados")
        db_table = 'dado'

    def __str__(self):
        return f'{self.id_contrato}, {self.vendedor}'

    def get_absolute_url(self):
        return reverse("Dado_detail", kwargs={"pk": self.pk})


class RepasseAprovado(models.Model):
    cliente = models.ForeignKey('Pessoas', on_delete=models.CASCADE, blank=True, null=True)
    repasses = models.ManyToManyField(Dado, blank=True)
    repasses_retidos = models.ManyToManyField("home.RepasseRetido", verbose_name=_("repasses_retidos"))
    creditos = models.ManyToManyField("home.Credito", verbose_name=_("creditos"))
    debitos = models.ManyToManyField("home.Debito", verbose_name=_("debitos"))
    taxas = models.ManyToManyField("home.Taxa", verbose_name=_("taxas"))
    parcelas_taxas = models.ManyToManyField("home.ParcelaTaxa", verbose_name=_("parcelas_taxas"))
    data_inicial = models.DateField(_(""), blank=True, null=True)
    data_final = models.DateField(_(""), blank=True, null=True)
    data_aprovado = models.DateTimeField(_(""), blank=True, null=True, auto_now_add=True)
    
    def total_repasses_retidos(self):
        return self.repasses_retidos.aggregate(Sum('vlr_rep_retido'))['vlr_rep_retido__sum'] or 0
    
    def total_creditos(self):
        #unsupported operand type(s) for +: 'NoneType' and 'decimal.Decimal'
        credito_parcelas_taxas = self.parcelas_taxas.filter(id_vendedor=self.cliente.id).aggregate(Sum('repasse'))['repasse__sum'] or 0
        total_creditos = self.creditos.aggregate(Sum('vl_credito'))['vl_credito__sum'] or 0
        return (total_creditos or 0) + credito_parcelas_taxas
    
    def total_debitos(self):
        debito_parcelas_taxas = self.parcelas_taxas.filter(id_comprador = self.cliente.id).aggregate(Sum('desconto_total'))['desconto_total__sum'] or 0
        total_debito = self.debitos.aggregate(Sum('vl_debito'))['vl_debito__sum'] or 0
        return (total_debito or 0) + (debito_parcelas_taxas or 0)
    
    def total_taxas(self):
        return self.taxas.aggregate(Sum('taxas'))['taxas__sum'] or 0
    
    def todos_os_repasses(self):
        return self.repasses.aggregate(Sum('repasses'))['repasses__sum'] or 0
    
    def total_repasse(self) -> decimal.Decimal:
        return self.total_creditos() - self.total_taxas() + self.todos_os_repasses() - self.total_debitos() + self.total_repasses_retidos()
    def __str__(self):
        return f'{self.total_repasse()}'

    class Meta:
        db_table = 'repasses_aprovados'
        managed = True
        verbose_name = 'RepasseAprovado'
        verbose_name_plural = 'RepasseAprovados'
        ordering = ['id']

class ParcelaTaxa(models.Model):
    id_contrato = models.IntegerField(_(""), blank=True, null=True)
    id_comprador = models.IntegerField(_(""), blank=True, null=True)
    comprador = models.CharField(_("Nome do comprador "), max_length=128, blank=True, null=True)
    id_vendedor= models.IntegerField(_(""), blank=True, null=True)
    vendedor = models.CharField(_("Nome do vendedor "), max_length=128, blank=True, null=True)
    parcela = models.CharField(_(""), max_length=128, blank=True, null=True)
    dt_vencimento = models.DateField(_(""), blank=True, null=True)
    valor = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    tcc = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    desconto_total = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    honorarios = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    repasse = models.DecimalField(_(""), max_digits=12, decimal_places=2, blank=True, null=True)
    aprovada = models.BooleanField(_(""), blank=True, null=True, default=False)
    aprovada_para_repasse = models.BooleanField(_(""), default=False, blank=True, null=True)
    data_aprovada = models.DateField(_(""), blank=True, null=True)
    criado = models.DateTimeField(_(""), auto_now_add=True, blank=True, null=True)
    #ParcelaTaxa.objects.filter(data_criado=datetime.date.today())
    
    def __str__(self):
        return f'{self.id_contrato}, {self.comprador}'

    class Meta:
        db_table = 'parcela_taxa'
        managed = True
        verbose_name = 'ParcelaTaxa'
        verbose_name_plural = 'ParcelaTaxas'
        
auditlog.register(CadCliente)
auditlog.register(RepasseRetido)
auditlog.register(Debito)
auditlog.register(Credito)
auditlog.register(Taxa)
auditlog.register(RepasseAprovado)

#? Remover caso a quantidade seja absurda de grande quantidade de dados de entrada para os modelos Dado e ParcelaTaxa
auditlog.register(Dado)
auditlog.register(ParcelaTaxa)