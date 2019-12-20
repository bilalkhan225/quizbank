from django.contrib import admin
from .models import *


class q_aadmin(admin.ModelAdmin):
    list_display = ('Question', 'CorAns')


admin.site.register(q_a, q_aadmin)
