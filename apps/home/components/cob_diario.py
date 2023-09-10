from datetime import datetime, date, timedelta
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch
from django.db.models.functions import Coalesce, Cast
from decimal import Decimal
from django_unicorn.components import UnicornView, QuerySetType
from django.contrib.humanize.templatetags.humanize import intcomma

from apps.home.models import Credito, Debito
from apps.home.existing_models import Pessoas

from django_unicorn.components import UnicornView, QuerySetType

from apps.home.models import Credito, Debito
from apps.home.existing_models import ContratoParcelas, Pessoas

class CobDiarioView(UnicornView):
    #?campos de filtro
    data_inicio: str = ""
    data_fim: str = ""
    contrato_id: int = None
    #?queryset
    parcelas: QuerySetType[ContratoParcelas] = ContratoParcelas.objects.none()
    
    def filtrar_parcelas(self):
        print(self.contrato_id, self.data_inicio, self.data_fim)
        if self.data_inicio != "" and self.data_fim != "":
            print("POSSUI DATA INICIO E FIM")
            self.parcelas = ContratoParcelas.objects.filter(
                contratos__id=self.contrato_id,
                dt_pagto__range=[self.data_inicio, self.data_fim],
                aprovada=False,
                aprovada_para_repasse=False,
            )
        else:
            print("NÃO POSSUI DATAS, IREI FILTARR SOMENTE PELO ID")
            if self.contrato_id:
                self.parcelas = ContratoParcelas.objects.filter(
                    contratos__id=self.contrato_id,
                    aprovada=False,
                    aprovada_para_repasse=False,
                ).select_related("contratos")
                
    def aprovar_parcela(self, parcela_id):
        parcela = ContratoParcelas.objects.get(id=parcela_id)
        parcela.aprovada = True
        parcela.save()
        self.filtrar_parcelas()