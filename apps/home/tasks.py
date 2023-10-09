from celery import shared_task
from celery.schedules import crontab
from core.celery import app
from datetime import datetime

@app.task(name="criar_dados")
def criar_dados():
    return "FUNCIONANDO"


@app.task
def escrever_em_arquivo():
    now = datetime.now()
    data_hora = now.strftime("%Y-%m-%d %H:%M:%S")
    
    with open("log.txt", "a") as arquivo:  # O modo "a" permite adicionar ao arquivo existente
        arquivo.write(data_hora + "\n")



""" @app.task(bind=True)
def agendar_tarefa_criar_dados(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*"),
        criar_dados.s(),
        name="criar_dados",
    ) """