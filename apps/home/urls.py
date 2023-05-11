# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views, views_fix_repasse


app_name = 'home'
""" urlpatterns = [
    # The home page
    path('', views.index, name='home'),

    path("upload_planilha_quinzenal", views.upload_planilha_quinzenal,
         name="upload_planilha_quinzenal"),
    path("download_planilha_repasses", views.download_planilha_repasses,
         name="download_planilha_repasses"),

    path("download_planilha_cob", views.download_planilha_cob,
         name="download_planilha_cob"),
    path("upload_planilha_cob", views.upload_planilha_cob,
         name="upload_planilha_cob"),
    path("upload_planilha_cavalos_cob", views.upload_planilha_cavalos_cob,
         name="upload_planilha_cavalos_cob"),
    path("upload_planilha_cad_clientes", views.upload_planilha_cad_clientes,
         name="upload_planilha_cad_clientes"),
    path("upload_planilha_parcelas_taxas", views.upload_planilha_parcelas_taxas,
         name="upload_planilha_parcelas_taxas"),
    path("upload_planilha_dados_brutos", views.upload_planilha_dados_brutos,
         name="upload_planilha_dados_brutos"),
    path('aprovar_repasse/<id_vendedor>/<data_inicial>/<data_final>/<total_repasse_retido>/<total_credito>/<total_taxa>/<total_debito>/<total_repasse>',
         views.aprovar_repasse, name="aprovar_repasse"),
    path('aprovar_parcela_taxa/<parcela_taxa_id>/<data_inicio>/<data_fim>',
         views.aprovar_parcela_taxa, name="aprovar_parcela_taxa"),
    path('desaprovar_repasse/<repasse_aprovado_id>',
         views.desaprovar_repasse, name="desaprovar_repasse"),
    path('aprovar-taxa-manual/<taxa_id>',views.aprovar_taxa_manual, name="aprovar_taxa_manual"),
    path('desaprovar_parcela_taxa/<parcela_taxa_id>/',views.desaprovar_parcela_taxa, name="desaprovar_parcela_taxa"),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

] """

urlpatterns = [

    # The home page
    path('', views_fix_repasse.index, name='home'),

    path("upload_planilha_quinzenal", views_fix_repasse.upload_planilha_quinzenal,
         name="upload_planilha_quinzenal"),
    path("download_planilha_repasses", views_fix_repasse.download_planilha_repasses,
         name="download_planilha_repasses"),

    path("download_planilha_cob", views_fix_repasse.download_planilha_cob,
         name="download_planilha_cob"),
    path("upload_planilha_cob", views_fix_repasse.upload_planilha_cob,
         name="upload_planilha_cob"),
    path("upload_planilha_cavalos_cob", views_fix_repasse.upload_planilha_cavalos_cob,
         name="upload_planilha_cavalos_cob"),
    path("upload_planilha_cad_clientes", views_fix_repasse.upload_planilha_cad_clientes,
         name="upload_planilha_cad_clientes"),
    path("upload_planilha_parcelas_taxas", views_fix_repasse.upload_planilha_parcelas_taxas,
         name="upload_planilha_parcelas_taxas"),
    path("upload_planilha_dados_brutos", views_fix_repasse.upload_planilha_dados_brutos,
         name="upload_planilha_dados_brutos"),
    path('aprovar_repasse/<id_pessoa>/<data_inicio>/<data_fim>',
         views_fix_repasse.aprovar_repasse, name="aprovar_repasse"),
    path('aprovar_parcela_taxa/<parcela_taxa_id>/<data_inicio>/<data_fim>',
         views_fix_repasse.aprovar_parcela_taxa, name="aprovar_parcela_taxa"),
    path('desaprovar_repasse/<repasse_aprovado_id>',
         views_fix_repasse.desaprovar_repasse, name="desaprovar_repasse"),
    path('aprovar-taxa-manual/<taxa_id>',
         views_fix_repasse.aprovar_taxa_manual, name="aprovar_taxa_manual"),
    path('desaprovar_parcela_taxa/<parcela_taxa_id>/',
         views_fix_repasse.desaprovar_parcela_taxa, name="desaprovar_parcela_taxa"),
    path('aprovar-credito/<credito_id>',
         views_fix_repasse.aprovar_credito, name='aprovar_credito'),
    path('desaprovar-credito/<credito_id>',
         views_fix_repasse.desaprovar_credito, name='desaprovar_credito'),
    path('aprovar-debito/<debito_id>',
         views_fix_repasse.aprovar_debito, name='aprovar_debito'),
    path('desaprovar-debito/<debito_id>',
         views_fix_repasse.desaprovar_debito, name='desaprovar_debito'),
    path('aprovar-repasse-retido/<repasse_retido_id>',
         views_fix_repasse.aprovar_repasse_retido, name='aprovar_repasse_retido'),
    path('desaprovar-repasse-retido/<repasse_retido_id>',
         views_fix_repasse.desaprovar_repasse_retido, name='desaprovar_repasse_retido'),
    # Matches any html file
    re_path(r'^.*\.*', views_fix_repasse.pages, name='pages'),

]
