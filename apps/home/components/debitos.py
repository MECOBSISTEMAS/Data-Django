from django.utils.text import slugify
from datetime import datetime, date, timedelta
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from decimal import Decimal
from openpyxl.utils import get_column_letter
from django_unicorn.components import UnicornView, QuerySetType

from apps.home.models import Debito, Credito
from apps.home.existing_models import Pessoas

class DebitosView(UnicornView):
    #? campos para filtrar pelas datas
    data_inicio:str = ""
    data_fim:str = ""
    #? campos para armazenar os resultados dos filtros
    debitos_nao_aprovadas:QuerySetType(Debito) = Debito.objects.none()
    debitos_aprovadas:QuerySetType(Debito) = Debito.objects.none()
    
    #?campos para construção da primeira tabela agrupando os resultados por dia
    debitos_dias:list = []
    debitos:QuerySetType(Debito) = Debito.objects.none()
    tbody:str = ""
    
    #?campos para adicionar novo debito
    id_pagador:str = ""
    id_credor:str = ""
    valor:float = None
    data_debito:str = ""
    descricao:str = ""
    
    #? campo para adicionar mensagem de erro ao adicionar novo debito
    mensagem_error_novo_debito:str = ""
    
    def filtrar_debitos(self):
        self.debitos_nao_aprovadas = Debito.objects.filter(aprovada=False, dt_debitado__range=[self.data_inicio, self.data_fim])
        self.debitos_aprovadas = Debito.objects.filter(aprovada=True, dt_debitado__range=[self.data_inicio, self.data_fim])
        
        debito_dias = {}
        for i in range((datetime.strptime(self.data_fim, '%Y-%m-%d') - datetime.strptime(self.data_inicio, '%Y-%m-%d')).days + 1):
            dia = datetime.strptime(self.data_inicio, '%Y-%m-%d') + timedelta(days=i)
            debito_dias[f'{dia.day}/{dia.month}/{dia.year}'] = Sum(
                Case(
                    When(dt_debitado__day=dia.day, then=F('vl_debito')),
                    default=0,
                    output_field=DecimalField(),
                ),
            )
        self.debitos_dias = list(debito_dias.keys())
        self.debitos = Debito.objects.filter(
            dt_debitado__range=[self.data_inicio, self.data_fim]
        ).values('cliente__nome', 'cliente_id').annotate(
            **debito_dias, 
            total_debito=Sum('vl_debito')
        ).order_by('cliente_id')
        
        tbody = ""
        for debito in self.debitos:
            tbody += "<tr>"
            tbody += f"<td>{debito['cliente_id']}</td>"
            tbody += f"<td>{debito['cliente__nome']}</td>"
            for dia in self.debitos_dias:
                tbody += f"<td>{debito[dia]}</td>"
            tbody += f"<td>{debito['total_debito']}</td>"
            tbody += "</tr>"
        self.tbody = tbody
    
    def novo_debito(self):
        try:
            pessoa = Pessoas.objects.get(id=self.id_pagador)
            novo_debito = Debito.objects.create(
                cliente=pessoa,
                vl_debito=self.valor,
                descricao=self.descricao,
                dt_debitado=self.data_debito,
            )
            if self.id_credor is not None and self.id_credor != "":
                credor = Pessoas.objects.get(id=self.id_credor)
                Credito.objects.create(
                    cliente=credor,
                    vl_credito=self.valor,
                    descricao=self.descricao,
                    dt_creditado=self.data_debito,
                )
            self.mensagem_error_novo_debito = ""
        except Pessoas.DoesNotExist:
            self.mensagem_error_novo_debito = "Pagador não encontrado"
        self.filtrar_debitos()
        
    def aprovar_debito(self, id_debito):
        debito = Debito.objects.get(id=id_debito)
        debito.aprovada = True
        debito.save()
        self.filtrar_debitos()
        
    def desaprovar_debito(self, id_debito):
        debito = Debito.objects.get(id=id_debito)
        debito.aprovada = False
        debito.save()
        self.filtrar_debitos()
    
    def deletar_debito(self, id_debito):
        debito = Debito.objects.get(id=id_debito)
        debito.delete()
        self.filtrar_debitos()