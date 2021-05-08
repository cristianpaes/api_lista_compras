from django.contrib import admin
from compras.models import ComprasItem

@admin.register(ComprasItem)
class ComprasAdmin(admin.ModelAdmin):
     list_display = ['id','nome','quantidade']
