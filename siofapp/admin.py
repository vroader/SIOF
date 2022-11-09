from django.contrib import admin
from django.utils.translation import gettext_lazy as _
#from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.db import models
from django.forms import TextInput, Textarea
from .models import TblCadastrodemandas, TblFcdfempenho,\
     TblFcdfplanointernoorcamento,\
     TblGdfcreditosorcamentarios,\
     TblGdfempenho, TblGdfpiocreditosorcamentarios,\
     TblGdfplanointernoorcamento,\
     TblItemaquisicaoservico,\
     TblCoordenadoressetoriais,\
     TblFcdfempenho,\
     TblFcdfitemempenho,\
     TblProcessoaquisicaoservico,\
     TblPrevisaofaseexecucao,\
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

class coordenadoresAdmin (admin.ModelAdmin):
    list_display = ('cso_codigo', 'cso_nome')
    list_filter = ('cso_status__sta_descricao',)

admin.site.register(TblCoordenadoressetoriais, coordenadoresAdmin)

class faseAquisicaoInline(admin.TabularInline):
    model = TblPrevisaofaseexecucao

class itemAquisicaoInline(admin.TabularInline):
    model = TblItemaquisicaoservico
    formfield_overrides= {
        models.CharField: {'widget':TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    #fields  = ['itg_itemaquisicao', ('itg_descricao', 'itg_operacao', 'itg_quantidade', 'itg_valor', 'itg_data')]
    
class tblProcessoaquisicaoservicoAdmin(admin.ModelAdmin):
    inlines = [itemAquisicaoInline, faseAquisicaoInline, ]

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
    inlines= [gdfpiocretidosorcamentarios, ]
    model= TblGdfcreditosorcamentarios
    extra=1
    #formfield_overrides: Mapping[Type[Field[Any, Any]], Mapping[str, Any]]

class GdfplanointernoorcamentoAdmin(admin.ModelAdmin):
    inlines = [gdfpiocretidosorcamentarios, ]
    class Meta:
        model = TblGdfplanointernoorcamento
    #def get_gdfcreditos(self, obj):
    #    return "\n".join([p.id_gdfcreditosorcamentarios for p in obj.credito.all()])
    #get_gdfcreditos.short_description = "Creditos"
   
admin.site.register(TblGdfcreditosorcamentarios, gdfcreditosorcamentariosAdmin)
admin.site.register(TblGdfplanointernoorcamento, GdfplanointernoorcamentoAdmin)
admin.site.register(TblGdfpiocreditosorcamentarios)

