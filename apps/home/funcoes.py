from datetime import datetime, timedelta
from django.db.models import Sum, Case, When, F, DecimalField

def construir_dias_filtro(data_inicio:str, data_fim:str, dt_vencimento, campo:str) -> dict:
	dias_context = {}
	for i in range((datetime.strptime(data_fim, '%Y-%m-%d') - datetime.strptime(data_inicio, '%Y-%m-%d')).days + 1):
		dia = datetime.strptime(data_inicio, '%Y-%m-%d') + timedelta(days=i)
		dias_context[f'dia_{dia.day}'] = Sum(
			Case(
				When(dt_vencimento__day=dia.day, then=F(campo)),
				default=0,
				output_field=DecimalField(decimal_places=2, max_digits=14, validators=[]),
			),
		)
	return dias_context
