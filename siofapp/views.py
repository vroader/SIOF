from django.shortcuts import render
from django.http import HttpResponse
from siofapp.models import viw_qddfcdf2, TblFcdfplanointernoorcamento, TblCadastrodemandas, TblFcdfremanejamento
from django.db.models.aggregates import Avg, Sum

# Create your views here.
def home(request):
    data = { }
    data['db'] = viw_qddfcdf2.objects.all().order_by('Ordenador')
    return render(request, 'index.html', data)
'''
def vpio(request):
    data = { }
    #cadastro = { }
    #data['db'] = TblFcdfplanointernoorcamento.objects.select_related('pif_cadastrodemanda').filter(pif_exercicio = 2022)
    #TblFcdfplanointernoorcamento.objects.select_related('pif_cadastrodemanda').filter(pif_exercicio=2022)
    data['db'] = TblFcdfplanointernoorcamento.objects.all().filter(pif_exercicio=2022)
    #cadastro['demandas'] = TblCadastrodemandas.objects.all()
    return render(request, 'pio.html', data)
'''
def pioView(request, cso):
    pioCso = TblFcdfplanointernoorcamento.objects.filter(pif_cadastrodemanda__cad_coordenadorsetorial=cso).filter(pif_exercicio = 2022)
    pioPessoal = TblFcdfplanointernoorcamento.objects.filter(pif_cadastrodemanda__cad_fcdfdespesadetalhada__nfc_grupodespesa=1).filter(pif_cadastrodemanda__cad_coordenadorsetorial=cso).filter(pif_exercicio = 2022)
    pioCusteio = TblFcdfplanointernoorcamento.objects.filter(pif_cadastrodemanda__cad_fcdfdespesadetalhada__nfc_grupodespesa=3).filter(pif_cadastrodemanda__cad_coordenadorsetorial=cso).filter(pif_exercicio = 2022)
    pioInvestimento = TblFcdfplanointernoorcamento.objects.filter(
        pif_cadastrodemanda__cad_fcdfdespesadetalhada__nfc_grupodespesa=4).filter(
        pif_cadastrodemanda__cad_coordenadorsetorial=cso).filter(pif_exercicio=2022)
    somaCso = TblFcdfplanointernoorcamento.objects.filter(pif_cadastrodemanda__cad_coordenadorsetorial=cso).filter(pif_exercicio = 2022).aggregate(Sum('pif_valor'))
    return render(request, 'planoInterno.html', {'cso':cso, 'pioCso':pioCso, 'pioCusteio':pioCusteio, 'pioPessoal':pioPessoal, 'pioInvestimento':pioInvestimento, 'somaCso':somaCso['pif_valor__sum']})

def cadastroView(request, cso):
    cadastroCso = TblCadastrodemandas.objects.filter(cad_coordenadorsetorial__cso_codigo=cso).filter(cad_status=1).order_by('cad_codigodemanda')
    return render(request, 'cadastro.html', {'cso':cso, 'cadastroCso':cadastroCso})

def remanejamentoView(request):
    remanejamento = TblFcdfremanejamento.objects.all()
    return render(request, 'remanejamento.html', {'remanejamento': remanejamento})