from datetime import datetime, date, timedelta
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from decimal import Decimal
from django_unicorn.components import UnicornView, QuerySetType

from apps.home.models import RepasseRetido
from apps.home.existing_models import Pessoas

from django_unicorn.components import UnicornView


class RepassesRetidosView(UnicornView):
    #? campos para filtrar pelas datas
    data_inicio:str = ""
    data_fim:str = ""
    
    #? campos para armazenar os resultados dos filtros
    repasses_retidos_nao_aprovadas:QuerySetType(RepasseRetido) = RepasseRetido.objects.none()
    repasses_retidos_aprovadas:QuerySetType(RepasseRetido) = RepasseRetido.objects.none()
    
    #?campos para construção da primeira tabela agrupando os resultados por dia
    repasses_retidos_dias:list = []
    repasses_retidos:QuerySetType(RepasseRetido) = RepasseRetido.objects.none()
    tbody:str = ""
    
    #? campos para criar um novo RepasseRetido
    id_pessoa:str = ""
    valor:float = None
    data_repasse_retido:str = ""
    tipo_repasse_retido:str = ""
    
    mensagem_error_novo_repasse_retido:str = ""
    def filtrar_repasses_retidos(self):
        self.repasses_retidos_aprovadas = RepasseRetido.objects.filter(aprovada=True, dt_rep_retido__range=[self.data_inicio, self.data_fim])
        self.repasses_retidos_nao_aprovadas = RepasseRetido.objects.filter(aprovada=False, dt_rep_retido__range=[self.data_inicio, self.data_fim])
        
        repasses_retidos_dias = {}
        for i in range((datetime.strptime(self.data_fim, '%Y-%m-%d') - datetime.strptime(self.data_inicio, '%Y-%m-%d')).days + 1):
            dia = datetime.strptime(self.data_inicio, '%Y-%m-%d') + timedelta(days=i)
            repasses_retidos_dias[f'{dia.day}/{dia.month}/{dia.year}'] = Sum(
                Case(
                    When(dt_rep_retido=dia, then=F('vlr_rep_retido')),
                    default=0,
                    output_field=DecimalField(),
                ),
            )
        self.repasses_retidos_dias = list(repasses_retidos_dias.keys())
        self.repasses_retidos = RepasseRetido.objects.filter(
            dt_rep_retido__range=[self.data_inicio, self.data_fim]
        ).values('cliente__nome', 'cliente_id').annotate(
            **repasses_retidos_dias, 
            total_repasse_retido=Sum('vlr_rep_retido')
        ).order_by('cliente_id')
        
        tbody = ""
        for repasse_retido in self.repasses_retidos:
            tbody += "<tr>"
            tbody += f"<td>{repasse_retido['cliente_id']}</td>"
            tbody += f"<td>{repasse_retido['cliente__nome']}</td>"
            for dia in self.repasses_retidos_dias:
                tbody += f"<td>{repasse_retido[dia]}</td>"
            tbody += f"<td>{repasse_retido['total_repasse_retido']}</td>"
            tbody += "</tr>"
        self.tbody = tbody
        
    def novo_repasse_retido(self):
        try:
            pessoa = Pessoas.objects.get(id=self.id_pessoa)
            RepasseRetido.objects.create(
                cliente=pessoa,
                vlr_rep_retido=self.valor,
                dt_rep_retido=self.data_repasse_retido,
                tipo=self.tipo_repasse_retido,
            )
            self.mensagem_error_novo_repasse_retido = ""
        except Pessoas.DoesNotExist:
            self.mensagem_error_novo_repasse_retido = "Pessoa não encontrada"
        self.filtrar_repasses_retidos()
        
        
    def deletar_repasse_retido(self, id_repasse_retido):
        RepasseRetido.objects.get(id=id_repasse_retido).delete()
        self.filtrar_repasses_retidos()
        
    def aprovar_repasse_retido(self, id_repasse_retido):
        RepasseRetido.objects.filter(id=id_repasse_retido).update(aprovada=True)
        self.filtrar_repasses_retidos()
        
    def desaprovar_repasse_retido(self, id_repasse_retido):
        RepasseRetido.objects.filter(id=id_repasse_retido).update(aprovada=False)
        self.filtrar_repasses_retidos()