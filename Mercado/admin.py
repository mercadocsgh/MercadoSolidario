from django.contrib import admin

# Register your models here.
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    fields = ['categoria']
    list_display = ('categoria',)
    createonly_fields = ['categoria' ]
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(CategoriaAdmin, self).get_readonly_fields(request, obj))
        createonly_fields = list(getattr(self, 'createonly_fields', []))   
        if obj:  # editing an existing object
            readonly_fields.extend(createonly_fields)
        return readonly_fields

admin.site.register(Categoria,CategoriaAdmin)

class ProdutoSolidarioAdmin(admin.ModelAdmin):
    fields =['id_categoria','quantidade','unidade','preco_solidario','estoque_minimo','max_familia','essencial','ativo']
    list_display = ('id_categoria','quantidade','unidade','estoque_minimo','preco_solidario','max_familia','essencial','codigo_solidario','ativo')
    createonly_fields = ['id_categoria','quantidade','unidade' ]
    ordering = ['id_categoria','quantidade','unidade','ativo']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(ProdutoSolidarioAdmin, self).get_readonly_fields(request, obj))
        createonly_fields = list(getattr(self, 'createonly_fields', []))   
        if obj:  # editing an existing object
            readonly_fields.extend(createonly_fields)
        return readonly_fields

admin.site.register(ProdutoSolidario,ProdutoSolidarioAdmin)

class CodBarProdSolAdmin(admin.ModelAdmin):
    fields =['id_produto','codigo_barras']
    list_display = ('id_produto','codigo_barras')
    ordering=['id_produto_id']

admin.site.register(CodBarProdSol,CodBarProdSolAdmin)

class FontesDoacaoAdmin(admin.ModelAdmin):
    fields =['nome','descricao']
    list_display = ('nome','descricao')
    createonly_fields = ['nome', ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(FontesDoacaoAdmin, self).get_readonly_fields(request, obj))
        createonly_fields = list(getattr(self, 'createonly_fields', []))   
        if obj:  # editing an existing object
            readonly_fields.extend(createonly_fields)
        return readonly_fields


admin.site.register(FonteDoacao,FontesDoacaoAdmin)

class AtendimentoTemplateAdmin(admin.ModelAdmin):
    fields = ('tipo','descricao')
    list_display = ('tipo','descricao')

admin.site.register(AtendimentoTemplate,AtendimentoTemplateAdmin)

class ItensAtendimentoTemplateAdmin(admin.ModelAdmin):
    fields = ('id_atendimento','id_produto','quantidade')
    list_display = ('id_atendimento','id_produto','quantidade')

admin.site.register(ItensAtendimentoTemplate,ItensAtendimentoTemplateAdmin)

class EstoqueAdmin(admin.ModelAdmin):
    fields = ('id_produto','validade','quantidade','quantidade_saida','id_fonte')
    list_display = ('id_produto','validade','quantidade','quantidade_saida','em_estoque','id_fonte')
    createonly_fields = ['id_produto','validade','quantidade_saida' ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(EstoqueAdmin, self).get_readonly_fields(request, obj))
        createonly_fields = list(getattr(self, 'createonly_fields', []))   
        if obj:  # editing an existing object
            readonly_fields.extend(createonly_fields)
        return readonly_fields

admin.site.register(Estoque,EstoqueAdmin)

class PessoasAtendimentoAdmin(admin.ModelAdmin):
    fields=('nome','qtd_pessoas','num_solidarios','ano','local','ativo')
    list_display=('nome','qtd_pessoas','num_solidarios','ano','local','ativo')

admin.site.register(PessoasAtendimento,PessoasAtendimentoAdmin)

class MotivoAdmin(admin.ModelAdmin):
    fields =['nome','descricao']
    list_display = ('nome','descricao')
    createonly_fields = ['nome', ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(MotivoAdmin, self).get_readonly_fields(request, obj))
        createonly_fields = list(getattr(self, 'createonly_fields', []))   
        if obj:  # editing an existing object
            readonly_fields.extend(createonly_fields)
        return readonly_fields
    
admin.site.register(Motivo,MotivoAdmin)
