from django.utils.text import slugify
from datetime import datetime, date, timedelta
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from django.contrib.humanize.templatetags.humanize import intcomma
import random
import ast
import tempfile
import os
import json
import openpyxl
from decimal import Decimal
from openpyxl.utils import get_column_letter
from django_unicorn.components import UnicornView, QuerySetType

from apps.home.models import Taxa
from apps.home.existing_models import Pessoas

class TaxasView(UnicornView):
    data_inicio:str = "" #? esse campo serve para armazenar a data do input data_inicio
    data_fim:str = "" #? esse campo serve para armazenar a data do input data_fim
    taxas_nao_aprovadas:QuerySetType(Taxa) = Taxa.objects.none()#? esse campo serve para armazenar as taxas não aprovadas
    taxas_aprovadas:QuerySetType(Taxa) = Taxa.objects.none()#? esse campor serve para armazenar as taxas aprovadas
    
    taxas_dias:list = []
    taxas:QuerySetType(Taxa) = Taxa.objects.none()
    tbody:str = ""
    
    
    #!campos para adicionar nova taxa
    cliente_id:int = None
    valor:float = None
    data_taxa:str = ""
    descricao:str = ""
    tipo_taxa:str = "TBB - Taxa de baixa de boleto"
    
    #? mensagem de erro para adicionar nova taxa
    mensagem_error_nova_taxa:str = ""

    def filtrar_taxas(self):
        self.taxas_nao_aprovadas = Taxa.objects.filter(aprovada=False, dt_taxa__range=[self.data_inicio, self.data_fim])
        self.taxas_aprovadas = Taxa.objects.filter(aprovada=True, dt_taxa__range=[self.data_inicio, self.data_fim])
        
        taxas_dias = {}
        for i in range((datetime.strptime(self.data_fim, '%Y-%m-%d') - datetime.strptime(self.data_inicio, '%Y-%m-%d')).days + 1):
            dia = datetime.strptime(self.data_inicio, '%Y-%m-%d') + timedelta(days=i)
            taxas_dias[f'{dia.day}/{dia.month}/{dia.year}'] = Sum(
                Case(
                    When(dt_taxa__day=dia.day, then=F('taxas')),
                    default=0,
                    output_field=DecimalField(),
                ),
            )
        self.taxas_dias = list(taxas_dias.keys())

        self.taxas = Taxa.objects.filter(
            dt_taxa__range=[self.data_inicio, self.data_fim]
        ).values(
            'cliente_id', 'cliente__nome'
        ).annotate(
            **taxas_dias,
            total_taxa=Sum('taxas')
        ).order_by('cliente_id')
        
        tbody = ""
        for taxa in self.taxas:
            tbody += "<tr>"
            tbody += f"<td>{taxa['cliente_id']}</td>"
            tbody += f"<td>{taxa['cliente__nome']}</td>"
            for dia in self.taxas_dias:
                formatted_taxa_dia = intcomma(taxa[dia]) #if isinstance(taxa[dia], int) else taxa[dia]
                tbody += f"<td>{formatted_taxa_dia}</td>"
            #tbody += f"<td>{taxa['total_taxa']}</td>"
            formated_total_taxa = intcomma(taxa['total_taxa'])
            tbody += f"<td>{formated_total_taxa}</td>"
            tbody += "</tr>"
        self.tbody = tbody

        
    
    def aprovar_taxa(self, id_taxa):
        taxa = Taxa.objects.get(id=id_taxa)
        taxa.aprovada = True
        taxa.data_aprovada = datetime.now()
        taxa.save()
        self.filtrar_taxas()
        
    def desaprovar_taxa(self, id_taxa):
        taxa = Taxa.objects.get(id=id_taxa)
        taxa.aprovada = False
        taxa.data_aprovada = None
        taxa.save()
        self.filtrar_taxas()
        
    def deletar_taxa(self, id_taxa):
        taxa = Taxa.objects.get(id=id_taxa)
        taxa.delete()
        self.filtrar_taxas()
        
    def nova_taxa(self):
        try:
            pessoa = Pessoas.objects.get(id=self.cliente_id)
            taxa = Taxa.objects.create(
                cliente=pessoa,
                taxas=self.valor,
                dt_taxa=self.data_taxa,
                descricao=self.descricao,
                tipo=self.tipo_taxa,
            )
            self.mensagem_error_nova_taxa = "Taxa adicionada com sucesso"
        except Pessoas.DoesNotExist:
            self.mensagem_error_nova_taxa = "Cliente não encontrado"
        except Exception as e:
            print(e)
        self.filtrar_taxas()
    
    """ def __del__(self):
        self.taxas_aprovadas = Taxa.objects.none()
        self.taxas_nao_aprovadas = Taxa.objects.none() """