from celery import shared_task
from celery.schedules import crontab
from core.celery import app
from datetime import datetime
from django.db.models.query_utils import Q
from apps.home.existing_models import ContratoParcelas
import asyncio
import requests
from asgiref.sync import sync_to_async

@app.task(name="criar_dados")
def criar_dados():
    return "FUNCIONANDO"


@app.task
def escrever_em_arquivo():
    now = datetime.now()
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a") as arquivo:  # O modo "a" permite adicionar ao arquivo existente
        arquivo.write(data_hora + "\n")
@app.task
def atualizar_vl_pagto_das_parcelas():
    parcelas_sem_vl_pagto = ContratoParcelas.objects.filter(Q(vl_pagto=None) | Q(vl_pagto__lte=0))

    for parcela in parcelas_sem_vl_pagto:
        try:
            # Realize a solicitação HTTP para obter o vl_pagto
            response = requests.get('http://82.208.22.228:8000/contrato_parcelas/{}/'.format(parcela.id))
            
            # Verifique se a solicitação foi bem-sucedida (status 200)
            if response.status_code == 200:
                resultado_da_requisicao = response.json()
                
                # Atualize a parcela com o valor obtido
                parcela.vl_pagto = resultado_da_requisicao['vl_pagto']
                parcela.save()
            else:
                # Registre ou notifique sobre o erro de solicitação HTTP
                print(f"Erro ao obter dados para parcela {parcela.id}: {response.status_code}")
        
        except requests.RequestException as e:
            # Trate erros de solicitação, como conexões perdidas
            print(f"Erro de solicitação para parcela {parcela.id}: {str(e)}")


async def processar_parcela(parcela: ContratoParcelas):
    # Sua lógica de processamento aqui
    try:
        response = requests.get("http://82.208.22.228:8000/contrato_parcelas/{}/".format(parcela.id))
        parcela_atualizada = response.json()
        parcela.vl_pagto = parcela_atualizada["vl_pagto"]
        parcela.save()
    except Exception as e:
        print("Erro ao processar parcela: " + str(e))

async def processar_parcelas_async():
    parcelas_sem_vl_pagto = ContratoParcelas.objects.filter(Q(vl_pagto=None) | Q(vl_pagto__lte=0))
    
    # Crie tarefas assíncronas para processar as parcelas
    tasks = [processar_parcela(parcela) for parcela in parcelas_sem_vl_pagto]
    
    # Execute as tarefas paralelamente
    await asyncio.gather(*tasks)
    
@app.task
def executar_async():
    # Crie um loop de eventos para executar as tarefas
    asyncio.run(processar_parcelas_async())
""" @app.task(bind=True)
def agendar_tarefa_criar_dados(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*"),
        criar_dados.s(),
        name="criar_dados",
    ) """