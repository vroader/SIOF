from django.shortcuts import render
from django.http import HttpResponse
from siofapp.models import viw_gdfplanointerno,viw_fcdfplanointerno, viw_qddfcdf, viw_qddGdf, TblGdfquadrodetalhamentodespesa, TblFcdfplanointernoorcamento, TblCadastrodemandas, TblFcdfremanejamento, TblItemaquisicaoservico, TblFcdfitemempenho
from django.db.models.aggregates import Avg, Sum
from django.db.models import Sum

# Create your views here.
def home(request):
    data = { }
    data['db'] = viw_qddfcdf.objects.all().order_by('Ordenador')
    return render(request, 'index.html', data)

def quadroDetalhamento(request):
    total = viw_qddfcdf.objects.filter(Ano=2022).aggregate(lei=Sum('Lei') \
                , dotacaoInicial=Sum('DotacaoInicial') \
                , dotacaoAtual=Sum('DotacaoAtual') \
                , empenhado=Sum('Empenhado') \
                , liquidado=Sum('Liquidado') \
                , pago=Sum('Pago'))
    totalOrdenador = viw_qddfcdf.objects.filter(Ano=2022).values('Ordenador').annotate(lei=Sum('Lei')\
                ,dotacaoInicial=Sum('DotacaoInicial')\
                ,dotacaoAtual=Sum('DotacaoAtual')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado')\
                ,pago=Sum('Pago')).order_by('Ordenador')
    totalOrdenadorFonte = viw_qddfcdf.objects.filter(Ano=2022).values('Ordenador', 'Fonte' ).annotate(lei=Sum('Lei')\
                ,dotacaoInicial=Sum('DotacaoInicial')\
                ,dotacaoAtual=Sum('DotacaoAtual')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado')\
                ,pago=Sum('Pago')).order_by('Ordenador')
    totalOrdenadorFonteGrupo = viw_qddfcdf.objects.filter(Ano=2022).values('Ordenador', 'Fonte', 'Grupo' ).annotate(lei=Sum('Lei')\
                ,dotacaoInicial=Sum('DotacaoInicial')\
                ,dotacaoAtual=Sum('DotacaoAtual')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado')\
                ,pago=Sum('Pago')).order_by('Ordenador')
    return render(request, 'quadroDetalhamento.html', {'total':total\
                ,'totalOrdenador':totalOrdenador\
                ,'totalOrdenadorFonte':totalOrdenadorFonte\
                ,'totalOrdenadorFonteGrupo':totalOrdenadorFonteGrupo})

def quadroDetalhamentoGDF (request):                
    totalGdf = viw_qddGdf.objects.filter(Exercicio=2022).aggregate(lei=Sum('Lei')\
                ,alteracao=Sum('Alteracao')\
                ,despesaAutorizada=Sum('Autorizada')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado'))
    totalOrdenadorGdf = viw_qddGdf.objects.filter(Exercicio=2022).values('Ordenador').annotate(lei=Sum('Lei')\
                ,alteracao=Sum('Alteracao')\
                ,despesaAutorizada=Sum('Autorizada')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado'))
    totalOrdenadorFonteGdf = viw_qddGdf.objects.filter(Exercicio=2022).values('Ordenador', 'Fonte').annotate(lei=Sum('Lei')\
                ,alteracao=Sum('Alteracao')\
                ,despesaAutorizada=Sum('Autorizada')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado'))
    totalOrdenadorFonteGrupoGdf = viw_qddGdf.objects.filter(Exercicio=2022).values('Ordenador', 'Fonte', 'Grupo').annotate(lei=Sum('Lei')\
                ,alteracao=Sum('Alteracao')\
                ,despesaAutorizada=Sum('Autorizada')\
                ,empenhado=Sum('Empenhado')\
                ,liquidado=Sum('Liquidado'))
    return render(request, 'quadroDetalhamentoGDF.html', {'totalGdf':totalGdf\
                ,'totalOrdenadorGdf':totalOrdenadorGdf\
                ,'totalOrdenadorFonteGdf':totalOrdenadorFonteGdf\
                ,'totalOrdenadorFonteGrupoGdf':totalOrdenadorFonteGrupoGdf})

def pioView(request, cso):
    pioCsoGDF = viw_gdfplanointerno.objects.filter(viw_coordenadorsetorial=cso, viw_pioexercicio = 2022)
    pioTotalGDF = pioCsoGDF.aggregate(totalPrevisao=Sum('viw_previsao'), totalEmpenhado=Sum('viw_empenhado'))
    pioGrupoGDF = pioCsoGDF.values('viw_grupo').annotate(previsaoGrupo = Sum('viw_previsao'), empenhoGrupo = Sum('viw_empenhado'))
    pioCsoFCDF = viw_fcdfplanointerno.objects.filter(viw_coordenadorsetorial=cso, viw_pioexercicio = 2022)
    pioTotalFCDF = pioCsoFCDF.aggregate(totalPrevisao=Sum('viw_previsao'), totalEmpenhado=Sum('viw_empenhado'))
    pioGrupoFCDF = pioCsoFCDF.values('viw_grupo').annotate(previsaoGrupo = Sum('viw_previsao'), empenhoGrupo = Sum('viw_empenhado'))
    totalPrevisao = pioTotalGDF['totalPrevisao'] if pioTotalGDF['totalPrevisao'] != None else 0 + pioTotalFCDF['totalPrevisao'] if pioTotalGDF['totalPrevisao'] != None else 0
    totalEmpenhado = pioTotalGDF['totalEmpenhado'] if pioTotalGDF['totalEmpenhado'] != None else 0 + pioTotalFCDF['totalEmpenhado'] if pioTotalFCDF['totalEmpenhado'] != None else 0
    return render(request, 'planoInterno.html', {'cso':cso,\
     'pioCsoGDF':pioCsoGDF,\
     'pioTotalGDF': pioTotalGDF,\
     'pioGrupoGDF': pioGrupoGDF,\
     'pioCsoFCDF': pioCsoFCDF,\
     'pioTotalFCDF': pioTotalFCDF,\
     'pioGrupoFCDF': pioGrupoFCDF,
     'totalPrevisao': totalPrevisao,
     'totalEmpenhado': totalEmpenhado})

def cadastroView(request,cso):
    cadastroCso = TblCadastrodemandas.objects.filter(cad_coordenadorsetorial__cso_codigo=cso).filter(cad_status=1).order_by('cad_codigodemanda')
    return render(request, 'cadastro.html', {'cso':cso, 'cadastroCso':cadastroCso})

def acompanhamentoView(request):
    acompanhamento = TblItemaquisicaoservico.objects.select_related('itf_itemaquisicaoservico')
    return render(request, 'acompanhamento.html', {'acompanhamento': acompanhamento})