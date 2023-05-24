from datetime import datetime, date, timedelta
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from decimal import Decimal
from django_unicorn.components import UnicornView, QuerySetType

from apps.home.models import Credito, Debito
from apps.home.existing_models import Pessoas

from django_unicorn.components import UnicornView, QuerySetType


class CreditosView(UnicornView):
    #? campos para filtrar pelas datas
    data_inicio:str = ""
    data_fim:str = ""
    
    #? campos para armazenar os resultados dos filtros
    creditos_nao_aprovadas:QuerySetType(Credito) = Credito.objects.none()
    creditos_aprovadas:QuerySetType(Credito) = Credito.objects.none()
    
    #?campos para construção da primeira tabela agrupando os resultados por dia
    creditos_dias:list = []
    creditos:QuerySetType(Credito) = Credito.objects.none()
    tbody:str = ""
    
    #?campos para adicionar novo debito
    id_pagador:str = ""
    id_credor:str = ""
    valor:float = None
    data_credito:str = ""
    descricao:str = ""
    
    mensagem_error_novo_credito:list = []
    
    def filtrar_creditos(self):
        self.creditos_nao_aprovadas = Credito.objects.filter(aprovada=False, dt_creditado__range=[self.data_inicio, self.data_fim])
        self.creditos_aprovadas = Credito.objects.filter(aprovada=True, dt_creditado__range=[self.data_inicio, self.data_fim])
        
        creditos_dias = {}
        for i in range((datetime.strptime(self.data_fim, '%Y-%m-%d') - datetime.strptime(self.data_inicio, '%Y-%m-%d')).days + 1):
            dia = datetime.strptime(self.data_inicio, '%Y-%m-%d') + timedelta(days=i)
            creditos_dias[f'{dia.day}/{dia.month}/{dia.year}'] = Sum(
                Case(
                    When(dt_creditado=dia, then=F('vl_credito')),
                    default=0,
                    output_field=DecimalField(),
                ),
            )
        self.creditos_dias = list(creditos_dias.keys())
        self.creditos = Credito.objects.filter(
            dt_creditado__range=[self.data_inicio, self.data_fim]
        ).values('cliente__nome', 'cliente_id').annotate(
            **creditos_dias, 
            total_credito=Sum('vl_credito')
        ).order_by('cliente_id')
        
        tbody = ""
        for credito in self.creditos:
            tbody += "<tr>"
            tbody += f"<td>{credito['cliente_id']}</td>"
            tbody += f"<td>{credito['cliente__nome']}</td>"
            for dia in self.creditos_dias:
                tbody += f"<td>{credito[dia]}</td>"
            tbody += f"<td>{credito['total_credito']}</td>"
            tbody += "</tr>"
        self.tbody = tbody
        
        
    def novo_credito(self):
        try:
            credor = Pessoas.objects.get(id=self.id_credor)
            Credito.objects.create(
                cliente=credor,
                dt_creditado=self.data_credito,
                descricao=self.descricao,
                vl_credito=self.valor,
            )
            if self.id_pagador != self.id_credor and self.id_pagador != "" and self.id_pagador != None:
                pagador = Pessoas.objects.get(id=self.id_pagador)
                Debito.objects.create(
                    cliente=pagador,
                    dt_debitado=self.data_credito,
                    descricao=self.descricao,
                    vl_debito=self.valor,
                )
            self.mensagem_error_novo_credito.append('Credito adicionado com sucesso')
        except Pessoas.DoesNotExist:
            self.mensagem_error_novo_credito.append("Credor ou pagador não encontrado")
        self.filtrar_creditos()
            
    def aprovar_credito(self, id_credito):
        credito = Credito.objects.get(id=id_credito)
        credito.aprovada = True
        credito.save()
        self.filtrar_creditos()
        
    def desaprovar_credito(self, id_credito):
        credito = Credito.objects.get(id=id_credito)
        credito.aprovada = False
        credito.save()
        self.filtrar_creditos()
        
    def deletar_credito(self, id_credito):
        credito = Credito.objects.get(id=id_credito)
        credito.delete()
        self.filtrar_creditos()