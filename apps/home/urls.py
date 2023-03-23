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
    
    path("consulta_por_data",views.consulta_por_data, name="consulta_por_data"),
    path("criar_cad_cliente",views.criar_cad_cliente, name="criar_cad_cliente"),
    path('criar_novo_cadastro_de_credito_e_debito', 
        views.criar_novo_cadastro_de_credito_e_debito,
        name="criar_novo_cadastro_de_credito_e_debito"
    ),
    path("criar_nova_taxa", views.criar_nova_taxa, name="criar_nova_taxa"),
    path("criar_novo_repasse_retido", 
        views.criar_novo_repasse_retido, 
        name="criar_novo_repasse_retido"
    ),
    path("filtrar_tabela_quinzenal",
        views.filtrar_tabela_quinzenal,
        name="filtrar_tabela_quinzenal"
    ),
    path("upload_planilha_quinzenal", views.upload_planilha_quinzenal, name="upload_planilha_quinzenal"),
    path("download_planilha_quinzenal", views.download_planilha_quinzenal, name="download_planilha_quinzenal"),
    
    path("download_planilha_cob", views.download_planilha_cob, name="download_planilha_cob"),
    path("upload_planilha_cob", views.upload_planilha_cob, name="upload_planilha_cob"),
    path("upload_planilha_cavalos_cob", views.upload_planilha_cavalos_cob, name="upload_planilha_cavalos_cob"),
    path("upload_planilha_cad_clientes", views.upload_planilha_cad_clientes, name="upload_planilha_cad_clientes"),
    path("upload_planilha_parcelas_taxas", views.upload_planilha_parcelas_taxas, name="upload_planilha_parcelas_taxas"),
    path("upload_planilha_dados_brutos", views.upload_planilha_dados_brutos, name="upload_planilha_dados_brutos"),
    path('pagar_dado/<id>', views.pagar_dado, name="pagar_dado"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
