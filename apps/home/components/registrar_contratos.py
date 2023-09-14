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

from apps.home.existing_models import Contratos, ContratoParcelas, Pessoas, Eventos, Peso
from apps.home.models import CadCliente, Debito, Credito, Taxa, RepasseRetido, Dado, RepasseAprovado, ParcelaTaxa

from django_unicorn.components import UnicornView, QuerySetType


class RegistrarContratosView(UnicornView):
    #validadores booleanos
    pessoa_existe:bool = False
    contrato_existe:bool = False
    comprador_contrato_existe:bool = False
    vendedor_contrato_existe:bool = False
    #campos para registros
    id_pessoa:int = None
    peso:float = 0
    id_contrato:int = None
    adi:str = "sim"
    me:int = None
    op:int = None
    id_comissionado:int = None
    eh_condominio:str = "sim"
    #listas de objetos
    data:dict = None
    listas_pessoas:list = []
    pessoa:Pessoas = None
    contrato:Contratos = Contratos.objects.none()
    
    def checar_contrato(self):
        url = f'http://82.208.22.228:8000/ContratosAllContratoParcelasAllViewSet/{self.id_contrato}'
        response = requests.get(url=url)
        if response.ok:
            self.contrato_existe = True
            self.data = response.json()
            self.comprador_contrato_existe = Pessoas.objects.filter(id=self.data['comprador']).exists()
            self.vendedor_contrato_existe = Pessoas.objects.filter(id=self.data['vendedor']).exists()
        else:
            self.contrato_existe = False
            self.comprador_contrato_existe = False
            self.vendedor_contrato_existe = False
        response.close()
        
    
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
                #self.listas_pessoas.append(self.pessoa)
                self.listas_pessoas.append({'nome': self.pessoa.nome,'id':self.pessoa.id, 'peso': self.peso})
                #self.listas_pessoas[self.pessoa.id]['peso'] = self.peso
                self.pessoa = None
                self.id_pessoa = None
                self.pessoa_existe = False
                self.peso = 0
            else:
                print('pessoa ja existe no diciionario')
                
    def remover_pessoa(self, pessoa_id):
        if pessoa_id:
            for pessoa in self.listas_pessoas:
                if pessoa['id'] == pessoa_id:
                    self.listas_pessoas.remove(pessoa)
                    break
        
        
    
    def novo_contrato(self):
        if self.contrato_existe:
            contrato = Contratos.objects.create(
                id = self.data['id'],
                dt_contrato = self.data['dt_contrato'],
                vl_contrato = self.data['vl_contrato'],
                vendedor = Pessoas.objects.get(id=self.data['vendedor']),
                comprador = Pessoas.objects.get(id=self.data['comprador']),
                nu_parcelas = self.data['nu_parcelas'],
                vl_entrada = self.data['vl_entrada'],
                #eventos = self.data['eventos'],
                tp_contrato = self.data['tp_contrato'],
                #pessoas_id_inclusao = self.data['pessoas_id_inclusao'], #teria que importar todos os modelos do banco de dados de pessoas
                dt_inclusao = self.data['dt_inclusao'],
                honor_adimp = self.data['honor_adimp'],
                honor_inadimp = self.data['honor_inadimp'],
                status = self.data['status'],
                parcela_primeiro_pagto = self.data['parcela_primeiro_pagto'],
                juros = self.data['juros'],
                contratos_id_pai = self.data['contratos_id_pai'],
                dt_primeira_parcela = self.data['dt_primeira_parcela'],
                instrucao = self.data['instrucao'],
                termo_percentual_contrato = self.data['termo_percentual_contrato'],
                termo_descricao_lote = self.data['termo_descricao_lote'],
                termo_descricao_pagto = self.data['termo_descricao_pagto'],
                termo_local_data = self.data['termo_local_data'],
                termo_nomes_lote = self.data['termo_nomes_lote'],
                tp_contrato_boleto = self.data['tp_contrato_boleto'],
                gerar_boleto = self.data['gerar_boleto'],
                desconto_total = self.data['desconto_total'],
                fl_parcelas_zerado = self.data['fl_parcelas_zerado'],
                dt_parcelas_zerado = self.data['dt_parcelas_zerado'],
                motivo_zerado = self.data['motivo_zerado'],
                observacao_zerado = self.data['observacao_zerado'],
                dt_acao_judicial = self.data['dt_acao_judicial'],
                suspenso = self.data['suspenso'],
                dt_suspensao = self.data['dt_suspensao'],
                dt_retorno_suspensao = self.data['dt_retorno_suspensao'],
                repasse = self.data['repasse'],#! VALOR COMO: S/N
                status_antes_acordo = self.data['status_antes_acordo'],
                fiador = self.data['fiador'],
                animal = self.data['animal'],
                eh_condominio = True if self.eh_condominio == 'sim' else False,
            )
            for pessoa in self.listas_pessoas:
                pessoa_objeto = Pessoas.objects.get(id=pessoa['id'])
                contrato.vendedores.add(pessoa_objeto)
                for parcela in self.data['parcelas']:
                    parcela = ContratoParcelas.objects.create(
                        #id=parcela['id'],
                        contratos=contrato,
                        nu_parcela=parcela['nu_parcela'],
                        dt_vencimento=parcela['dt_vencimento'],
                        dt_pagto=parcela['dt_pagto'],
                        vl_parcela=parcela['vl_parcela'],
                        vl_correcao_monetaria=parcela['vl_correcao_monetaria'],
                        vl_juros=parcela['vl_juros'],
                        vl_pagto=parcela['vl_pagto'],
                        vl_juros_pagto=parcela['vl_juros_pagto'],
                        vl_honorarios=parcela['vl_honorarios'],
                        vl_taxa=parcela['vl_taxa'],
                        vl_multa=parcela['vl_multa'],
                        vl_corrigido=parcela['vl_corrigido'],
                        liquidada_no_cadastro=parcela['liquidada_no_cadastro'],
                        simulada=parcela['simulada'],
                        dt_vencimento_original=parcela['dt_vencimento_original'],
                        #arquivos_id_remessa=parcela['arquivos_id_remessa'],
                        nu_linha_remessa=parcela['nu_linha_remessa'],
                        #arquivos_id_retorno=parcela['arquivos_id_retorno'],
                        nu_linha_retorno=parcela['nu_linha_retorno'],
                        dt_credito=parcela['dt_credito'],
                        dt_processo_pagto=parcela['dt_processo_pagto'],
                        teds=parcela['teds'],
                        tratar_ted=parcela['tratar_ted'],
                        #pessoas_id_atualizacao=parcela['pessoas_id_atualizacao'],
                        fl_negativada=parcela['fl_negativada'],
                        motivo_zerado=parcela['motivo_zerado'],
                        observacao_zerado=parcela['observacao_zerado'],
                        fl_acao_judicial=parcela['fl_acao_judicial'],
                        boletos_avulso=parcela['boletos_avulso'],
                        dt_atualizacao_monetaria=parcela['dt_atualizacao_monetaria'],
                        eh_adi= True if self.adi == 'sim' else False,
                    )
                    Peso.objects.create(
                        pessoa=pessoa_objeto,
                        valor=pessoa['peso'],
                        parcela=parcela,
                        #adi=self.adi,
                        me=self.me,
                        op=self.op,
                    )
            
            self.id_contrato = None
            self.contrato_existe = False
            self.listas_pessoas = []
        else:
            print('contrato nao existe')
        

    def limpar_campos(self):
        self.adi = None
        self.me = None 
        self.op = None
        self.id_comissionado = None
        self.id_contrato = None
        self.contrato_existe = False
        self.comprador_contrato_existe = False
        self.vendedor_contrato_existe = False
        self.data = None
        self.listas_pessoas = []
        self.pessoa = None
        self.id_pessoa = None
        self.pessoa_existe = False
        self.peso = 0
        self.contrato = Contratos.objects.none()
