from datetime import datetime, date, timedelta
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from decimal import Decimal
from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.humanize.templatetags.humanize import intcomma

from apps.home.models import Credito, Debito, ParcelaTaxa
from apps.home.existing_models import Pessoas

from django_unicorn.components import UnicornView, QuerySetType


class ParcelasDeletadasView(UnicornView):
    #?campos do formulario
    data_vencimento_inicio:str = ""
    data_vencimento_fim:str = ""
    nome_vendedor:str = ""
    nome_comprador:str = ""
    #?campos para listar
    parcelas_taxas:QuerySetType[ParcelaTaxa] = ParcelaTaxa.objects.none()
    
    
    def filtrar_parcelas_taxas(self):
        query_params = {}
        if self.nome_comprador:
            query_params['comprador'] = self.nome_comprador
        if self.nome_vendedor:
            query_params['vendedor'] = self.nome_vendedor
        if self.data_vencimento_inicio:
            query_params['dt_vencimento__gte'] = self.data_vencimento_inicio
        if self.data_vencimento_fim:
            query_params['dt_vencimento__lte'] = self.data_vencimento_fim
        if len(query_params) > 0:
            self.parcelas_taxas = ParcelaTaxa.objects.filter(
                **query_params,
                aprovada=False,
                aprovada_para_repasse=False,
                deletada=True,
            )
            
    def restaurar_parcela_taxa(self, parcela_taxa_id:int):
        parcela_taxa = ParcelaTaxa.objects.get(id=parcela_taxa_id)
        parcela_taxa.deletada = False
        parcela_taxa.save()
        self.filtrar_parcelas_taxas()
        