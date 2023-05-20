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

class TaxasView(UnicornView):
    data_inicio:str = ""
    data_fim:str = ""
    taxas_nao_aprovadas:QuerySetType(Taxa) = Taxa.objects.none()
    taxas_aprovadas:QuerySetType(Taxa) = Taxa.objects.none()
    
    
    def filtrar_taxas(self):
        self.taxas_nao_aprovadas = Taxa.objects.filter(aprovada=False, dt_taxa__range=[self.data_inicio, self.data_fim])
        self.taxas_aprovadas = Taxa.objects.filter(aprovada=True, dt_taxa__range=[self.data_inicio, self.data_fim])

    
    """ def hydrate(self):
        self.call('reinitializeDataTables') """
        #return super().hydrate()
    
    def aprovar_taxa(self, id_taxa):
        taxa = self.taxas_nao_aprovadas.get(id=id_taxa)
        taxa.aprovada = True
        taxa.save()
        self.filtrar_taxas()
        
    def desaprovar_taxa(self, id_taxa):
        taxa = self.taxas_aprovadas.get(id=id_taxa)
        taxa.aprovada = False
        taxa.save()
        self.filtrar_taxas()
        
    def deletar_taxa(self, id_taxa):
        taxa = Taxa.objects.get(id=id_taxa)
        taxa.delete()
        self.filtrar_taxas()
    
    def __del__(self):
        self.taxas_aprovadas = Taxa.objects.none()
        self.taxas_nao_aprovadas = Taxa.objects.none()