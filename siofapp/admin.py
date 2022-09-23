from django.contrib import admin
from .models import TblCadastrodemandas,\
     TblFcdfplanointernoorcamento,\
     TblFcdfremanejamento,\
     TblGdfempenho,\
     TblGdfplanointernoorcamento,\
     TblItemaquisicaoservico,\
     TblProcessoaquisicaoservico,\
     TblCoordenadoressetoriais

# Register your models here.


admin.site.register(TblCadastrodemandas)
admin.site.register(TblGdfplanointernoorcamento)
admin.site.register(TblGdfempenho)
admin.site.register(TblProcessoaquisicaoservico)
admin.site.register(TblItemaquisicaoservico)
admin.site.register(TblFcdfremanejamento)
admin.site.register(TblCoordenadoressetoriais)

@admin.register(TblFcdfplanointernoorcamento)
class TblFcdfplanointernoorcamentoAdmin(admin.ModelAdmin):
    list_display = ("pif_cadastrodemanda", "pif_justificativa")
