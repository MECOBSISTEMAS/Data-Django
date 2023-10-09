import os

from celery.schedules import crontab
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core', broker="amqp://localhost")

app.conf.result_backend = 'rpc://'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

""" app.conf.beat_schedule = {
    'agendar-tarefa-criar-dados': {
        'task': 'apps.home.tasks.agendar_tarefa_criar_dados',
        'schedule': crontab(minute="*"),
    },
} """

app.conf.beat_schedule = {
    'agendar-escrever-em-arquivo': {
        'task': 'apps.home.tasks.escrever_em_arquivo',
        'schedule': crontab(minute="*"),
    }
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
