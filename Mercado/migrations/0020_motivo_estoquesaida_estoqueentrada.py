# Generated by Django 4.0.4 on 2025-04-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mercado', '0019_produtosolidario_ativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.CharField(max_length=255, verbose_name='descrição')),
            ],
            options={
                'verbose_name': 'Motivo da Saída',
                'verbose_name_plural': 'Motivos da Saída',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('data', models.DateField(auto_now_add=True, null=True)),
                ('quem_cadastrou', models.CharField(max_length=50)),
                ('comentario', models.CharField(max_length=255, null=True)),
                ('id_fonte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.fontedoacao', verbose_name='Fonte da Doação')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.produtosolidario')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.motivo')),
            ],
            options={
                'verbose_name': 'Estoque Saida',
                'verbose_name_plural': 'Estoque Saidas',
                'ordering': ['id_produto', 'validade', 'id_fonte'],
            },
        ),
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('validade', models.DateField()),
                ('data', models.DateField(auto_now_add=True, null=True)),
                ('quem_cadastrou', models.CharField(max_length=50)),
                ('id_fonte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.fontedoacao', verbose_name='Fonte da Doação')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Mercado.produtosolidario')),
            ],
            options={
                'verbose_name': 'Estoque Entrada',
                'verbose_name_plural': 'Estoque Entradas',
                'ordering': ['id_produto', 'validade', 'id_fonte'],
            },
        ),
    ]
