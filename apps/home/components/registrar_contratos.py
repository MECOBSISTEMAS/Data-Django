from optparse import Values
from django.utils.text import slugify
from datetime import datetime, date, timedelta
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db.models import Case, Sum, When, F, Q, IntegerField, DecimalField, OuterRef, Subquery, Value, Max, Prefetch, DateField, QuerySet
from django.db.models.functions import Coalesce, Cast, TruncMonth
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.core import serializers

from decimal import Decimal
from openpyxl.utils import get_column_letter
from requests import Request
import requests

from apps.home.existing_models import Contratos, ContratoParcelas, Pessoas, Eventos
from apps.home.models import CadCliente, Debito, Credito, Taxa, RepasseRetido, Dado, RepasseAprovado, ParcelaTaxa

from django_unicorn.components import UnicornView, QuerySetType


class RegistrarContratosView(UnicornView):
    #validadores booleanos
    pessoa_existe:bool = False
    contrato_existe:bool = False
    #campos para registros
    id_pessoa:int = None
    peso:float = 0
    id_contrato:int = None
    #listas de objetos
    listas_pessoas:list = []
    pessoa:Pessoas = None
    contrato:Contratos = Contratos.objects.none()
    
    def checar_contrato(self):
        sql_query = f"SELECT * FROM contratos WHERE contratos.id = {self.id_contrato};"
        response = requests.post('http://82.208.22.228:8000/execute_query_sql_class/', json={"sql": sql_query})
        print(response.json())
    
    def checar_pessoa(self):
        if self.id_pessoa:
            try:
                self.pessoa = Pessoas.objects.get(id=self.id_pessoa)
                self.pessoa_existe = True
            except:
                self.pessoa_existe = False
                
    def adicionar_pessoa(self):
        if self.pessoa:
            if self.pessoa.id not in self.listas_pessoas:
                print('irei adicionar a pessoa')
                #self.listas_pessoas.append(self.pessoa)
                self.listas_pessoas.append({'nome': self.pessoa.nome,'id':self.pessoa.id, 'peso': self.peso})
                #self.listas_pessoas[self.pessoa.id]['peso'] = self.peso
                self.pessoa = None
                self.id_pessoa = None
                self.pessoa_existe = False
                self.peso = 0
            else:
                print('pessoa ja existe no diciionario')
        
    
    def novo_contrato(self):
        print(f"POST: {self.request.POST}")
        pass
