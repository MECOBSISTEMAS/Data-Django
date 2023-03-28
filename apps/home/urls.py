# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

app_name = 'home'

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    
    path("upload_planilha_quinzenal", views.upload_planilha_quinzenal, name="upload_planilha_quinzenal"),
    path("download_planilha_quinzenal", views.download_planilha_quinzenal, name="download_planilha_quinzenal"),
    
    path("download_planilha_cob", views.download_planilha_cob, name="download_planilha_cob"),
    path("upload_planilha_cob", views.upload_planilha_cob, name="upload_planilha_cob"),
    path("upload_planilha_cavalos_cob", views.upload_planilha_cavalos_cob, name="upload_planilha_cavalos_cob"),
    path("upload_planilha_cad_clientes", views.upload_planilha_cad_clientes, name="upload_planilha_cad_clientes"),
    path("upload_planilha_parcelas_taxas", views.upload_planilha_parcelas_taxas, name="upload_planilha_parcelas_taxas"),
    path("upload_planilha_dados_brutos", views.upload_planilha_dados_brutos, name="upload_planilha_dados_brutos"),
    path('aprovar_repasse/<dados_consultados>/<data_inicial>/<data_final>', views.aprovar_repasse, name="aprovar_repasse"),
    path('desaprovar_repasse/<repasse_aprovado_id>', views.desaprovar_repasse, name="desaprovar_repasse"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
