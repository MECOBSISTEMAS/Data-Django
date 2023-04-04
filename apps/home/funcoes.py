from datetime import datetime
from django.utils.text import slugify
import tempfile
from datetime import datetime, timedelta
from django.db.models import Sum, Case, When, F, DecimalField
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import json


def construir_dias_filtro(data_inicio: str, data_fim: str, dt_vencimento, campo: str) -> dict:
    dias_context = {}
    for i in range((datetime.strptime(data_fim, '%Y-%m-%d') - datetime.strptime(data_inicio, '%Y-%m-%d')).days + 1):
        dia = datetime.strptime(data_inicio, '%Y-%m-%d') + timedelta(days=i)
        dias_context[f'dia_{dia.day}'] = Sum(
            Case(
                When(dt_vencimento__day=dia.day, then=F(campo)),
                default=0,
                output_field=DecimalField(
                    decimal_places=2, max_digits=14, validators=[]),
            ),
        )
    return dias_context


def gerar_arquivo_pdf(request, context):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        pdf = canvas.Canvas(tmp.name, initialFontSize=12,
                            initialFontName='Helvetica', pagesize=(595, 842))
        pdf.drawString(100, 750, "Relatório PDF do Prestação Diaria")
        #pdf.drawString(100, 700, "Adicione aqui os dados necessários")
        pdf.drawString(100, 650, request.session.get('comissionistas_do_mes'))
        pdf.drawString(100, 600, request.session.get('repasses_geral'))
        pdf.drawString(100, 550, request.session.get('repasses'))
        pdf.drawString(100, 500, request.session.get('comissoes'))
        pdf.drawString(100, 450, request.session.get(
            'valores_pagos_honorarios'))
        pdf.drawString(100, 400, request.session.get(
            'repasses_geral_descontado'))
        pdf.save()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="prestacao_diaria_pdf_{slugify(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}.pdf"'
        response.write(tmp.read())
        return response
