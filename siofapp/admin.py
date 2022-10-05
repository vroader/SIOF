from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import TblCadastrodemandas, TblFcdfempenho,\
     TblFcdfplanointernoorcamento,\
     TblFcdfremanejamento, TblGdfcreditosorcamentarios,\
     TblGdfempenho, TblGdfpiocreditosorcamentarios,\
     TblGdfplanointernoorcamento,\
     TblItemaquisicaoservico,\
     TblCoordenadoressetoriais,\
     TblFcdfempenho,\
     TblFcdfitemempenho,\
     TblProcessoaquisicaoservico,\
     TblGdfitemempenho

# Register your models here.


class CadastroDemandasAdmin (admin.ModelAdmin):
    list_display = ('cad_codigodemanda','cad_descricao')
    list_filter = ('cad_status__sta_descricao', 'cad_coordenadorsetorial')

admin.site.register(TblCadastrodemandas, CadastroDemandasAdmin)


class gdfItemEmpenho(admin.TabularInline):
    model = TblGdfitemempenho

class gdfEmpenhoAdmin(admin.ModelAdmin):
    inlines = [gdfItemEmpenho, ]

admin.site.register(TblGdfempenho, gdfEmpenhoAdmin)

class remanejamentoFcdfAdmin(admin.ModelAdmin):
    list_display = ('ref_especieremanejamento', 'ref_planointerno')

admin.site.register(TblFcdfremanejamento, remanejamentoFcdfAdmin)

class coordenadoresAdmin (admin.ModelAdmin):
    list_display = ('cso_codigo', 'cso_nome')
    list_filter = ('cso_status__sta_descricao',)

admin.site.register(TblCoordenadoressetoriais, coordenadoresAdmin)


class itemAquisicaoInline(admin.TabularInline):
    model = TblItemaquisicaoservico
    
class tblProcessoaquisicaoservicoAdmin(admin.ModelAdmin):
    inlines = [itemAquisicaoInline, ]

admin.site.register(TblProcessoaquisicaoservico, tblProcessoaquisicaoservicoAdmin)

class tblFcdfItemEmpenho(admin.TabularInline):
    model = TblFcdfitemempenho

class tblFcdfEmpenhoAdmin(admin.ModelAdmin):
    inlines = [tblFcdfItemEmpenho, ]

admin.site.register(TblFcdfempenho, tblFcdfEmpenhoAdmin)

class TblFcdfplanointernoorcamentoAdmin(admin.ModelAdmin):
    list_display = ('pif_cadastrodemanda', 'pif_data')
    list_filter = ('pif_exercicio', 'pif_cadastrodemanda__cad_coordenadorsetorial')

admin.site.register(TblFcdfplanointernoorcamento, TblFcdfplanointernoorcamentoAdmin)

class gdfpiocretidosorcamentarios(admin.TabularInline):
    model= TblGdfpiocreditosorcamentarios
    extra=1

class gdfcreditosorcamentariosAdmin(admin.ModelAdmin):
    inlines= [gdfpiocretidosorcamentarios,]
    model= TblGdfcreditosorcamentarios
    extra=1

class GdfplanointernoorcamentoAdmin(admin.ModelAdmin):
    inlines = [gdfpiocretidosorcamentarios,]
    def get_gdfcreditos(self, obj):
        return "\n".join([p.id_gdfcreditosorcamentarios for p in obj.TblGdfCreditosorcamentarios.all()])
   
admin.site.register(TblGdfcreditosorcamentarios, gdfcreditosorcamentariosAdmin)
admin.site.register(TblGdfplanointernoorcamento, GdfplanointernoorcamentoAdmin)

