from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .views import *
from django.http import HttpRequest,HttpResponse

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/logout',logout_view, name='Logout'),
    #path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ajuda/',TemplateView.as_view(template_name='ajuda.html'), name='Ajuda'),
    path('Estoque/',TemplateView.as_view(template_name='estoque/estoque.html'), name='Estoque MS CS'),
    path('Estoque/lista',estoque_listagem,name="Lista do Estoque MS CS" ),
    path('Estoque/listaProdSol',estoque_listagem_prodSol,name="Lista do Estoque por Produto Solidário MS CS" ),
    path('Estoque/listaValidade',estoque_listagem_validade,name="Lista do Estoque por Validade MS CS" ),
    path('Estoque/entrada/',TemplateView.as_view(template_name='estoque/entrada_estoque.html'),name="Cadastra Estoque MS CS" ),
    path('Estoque/entrada/codigo',entradaEstoque,name="Cadastra Estoque MS CS" ),
    path('Estoque/saida/',saidaEstoque,name='Saida de estoque'),
    path('Estoque/saida/codigo',saidaEstoqueCodigo,name='Saida de estoque codigo'),
    path('Estoque/listaentradas',listaEntradasEstoque,name='Lista de entradas de estoque'),
    path('Estoque/listasaidas',listaSaidasEstoque,name='Lista de saídas de estoque'),
    path('Atendimento/',TemplateView.as_view(template_name='atendimentos/atendimentos.html'),name='AtendimentoInicio'),
    path('Atendimento/mercado',informaSolidarios,name='Atendimentos'),
    path('Atendimento/mercadoCaixa',informaSolidariosCaixa,name='AtendimentosCaixa'),
    path('Atendimento/rascunho',iniciaRascunho,name='Inicia Rascunho'),
    path('Atendimento/rascunhoCaixa',iniciaRascunhoCaixa,name='Inicia Rascunho Caixa'),
    path('Atendimento/codigo',codigoMercado,name='Rascunho Mercado'),
    path('Atendimento/codigoCaixa',codigoMercadoCaixa,name='Rascunho Mercado Caixa'),
    path('Atendimento/cancelar',cancelarRascunho,name='Rascunho Mercado'),    
    path('Atendimento/removeritem/<int:id>',removerItem,name='remover Item rascunho'),
    path('Atendimento/aumentaritem/<int:id>',aumentarItem,name='Aumentar Item rascunho'),
    path('Atendimento/diminuiritem/<int:id>',diminuirItem,name='Diminuir Item rascunho'),
    path('Atendimento/concluir',concluirAtendimento,name='remover Item rascunho'),
    path('Atendimento/cestabasica',emDesenvolvimento,name='cesta básica'),
    path('Atendimento/cestaemergencial',emDesenvolvimento,name='cesta básica'),
    path('Relatorios',TemplateView.as_view(template_name='relatorios/relatorios.html'),name='Relatórios'),
    path('Relatorios/consumo-periodo',relatoriosConsumoPeriodo,name='Consumo por Período'),
    path('Relatorios/necessidade-periodo',relatoriosNecessidadePeriodo,name='Necessidade por Período'),
    path('Relatorios/atendimentosvoluntario',relatorioAtendimentoVoluntario,name='Atendimentos por Voluntario'),
    path('Relatorios/produtosporassistido',produtosEntreguesPorAssistido,name='Produtos Entregues por Assistido'),

]