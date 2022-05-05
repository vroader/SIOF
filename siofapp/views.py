from django.shortcuts import render
from django.http import HttpResponse
from siofapp.models import viw_qddfcdf2, TblFcdfplanointernoorcamento, TblCadastrodemandas

# Create your views here.
def home(request):
    data = { }
    data['db'] = viw_qddfcdf2.objects.all()
    return render(request, 'index.html', data)

def vpio(request):
    data = { }
    #cadastro = { }
    #data['db'] = TblFcdfplanointernoorcamento.objects.select_related('pif_cadastrodemanda').filter(pif_exercicio = 2022)
    #TblFcdfplanointernoorcamento.objects.select_related('pif_cadastrodemanda').filter(pif_exercicio=2022)
    data['db'] = TblFcdfplanointernoorcamento.objects.all().filter(pif_exercicio=2022)
    #cadastro['demandas'] = TblCadastrodemandas.objects.all()
    return render(request, 'pio.html', data)



