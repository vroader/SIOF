"""siofproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siofapp.views import home, pioView, cadastroView, remanejamentoView, acompanhamentoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    #path('pio', vpio),
    path('pio/<str:cso>/', pioView, name='planoInterno'),
    path('cadastro/<str:cso>/', cadastroView, name='cadastro'),
    path('remanejamento/', remanejamentoView, name='remanejamento'),
    path('acompanhamento/', acompanhamentoView, name='acompanhamento'),
]
