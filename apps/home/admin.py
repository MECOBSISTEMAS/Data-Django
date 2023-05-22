# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from apps.home.models import Credito, Debito, RepasseRetido, RepasseAprovado, Taxa, CadCliente
from apps.home.existing_models import Pessoas
# Register your models here.

admin.site.register(Credito)
admin.site.register(Debito)
admin.site.register(RepasseRetido)
admin.site.register(RepasseAprovado)
admin.site.register(Taxa)
admin.site.register(CadCliente)
admin.site.register(Pessoas)