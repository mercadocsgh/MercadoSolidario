select c.categoria, p.quantidade, p.unidade, p.preco_solidario, p.max_familia, p.codigo_solidario from Mercado_produtosolidario p, Mercado_categoria c where c.id = p.id_categoria_id order by categoria;

Select e.quantidade, e.quantidade_saida, e.quantidade - e.quantidade_saida as disponivel, e.validade, c.categoria, p.quantidade, p.unidade from Mercado_estoque e, Mercado_produtosolidario p, Mercado_cat
egoria c where c.id = p.id_categoria_id and p.id = e.id_produto_id order by e.quantidade;

grant all privileges on mercadosolidario.* to 'user'@'%';