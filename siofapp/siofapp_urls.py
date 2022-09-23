from django.urls import path
from .views import quadroDetalhamento, quadroDetalhamentoGDF

urlpatterns = [
    path("FCDF/", quadroDetalhamento, name="FCDF"),
    path("GDF/", quadroDetalhamentoGDF, name="GDF"),
    #path('<str:cso>/', pioView, name='planoInterno'),
]