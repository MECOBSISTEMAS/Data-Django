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
import random
import tempfile
import os
import json
import openpyxl
import asyncio
import calendar

from decimal import Decimal
from openpyxl.utils import get_column_letter
from requests import Request

from apps.home.existing_models import Contratos, ContratoParcelas, Pessoas, Eventos
from apps.home.models import CadCliente, Debito, Credito, Taxa, RepasseRetido, Dado, RepasseAprovado, ParcelaTaxa

from django_unicorn.components import UnicornView, QuerySetType


class RegistrarContratosView(UnicornView):
    #validadores booleanos
    pessoa_existe:bool = False
    contrato_existe:bool = False
    #campos para registros
    id_pessoa:int = None
    
    listas_pessoas:list[QuerySetType[Pessoas]] = []
    pessoa:Pessoas = None
    def checar_pessoa(self):
        if self.id_pessoa:
            try:
                self.pessoa = Pessoas.objects.get(id=self.id_pessoa)
                self.pessoa_existe = True
                print(self.pessoa)
            except:
                self.pessoa_existe = False
                
    def adicionar_pessoa(self):
        if self.pessoa:
            self.listas_pessoas = Pessoas.objects.filter(nome__icontains=self.pessoa.nome)
        
    
    def novo_contrato(self):
        pass
