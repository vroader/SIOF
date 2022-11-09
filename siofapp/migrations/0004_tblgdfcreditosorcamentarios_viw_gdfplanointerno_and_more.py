# Generated by Django 4.0.3 on 2022-10-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siofapp', '0003_viw_qddgdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblGdfcreditosorcamentarios',
            fields=[
                ('id_gdfcreditosorcamentarios', models.AutoField(db_column='id_GdfCreditosOrcamentarios', primary_key=True, serialize=False)),
                ('cog_exercicio', models.TextField(blank=True, db_column='cog_Exercicio', max_length=5, null=True)),
                ('cog_unidadeorcamentaria', models.CharField(blank=True, db_column='cog_UnidadeOrcamentaria', max_length=5, null=True)),
                ('cog_dataatualizacao', models.DateField(db_column='cog_DataAtualizacao')),
                ('cog_esfera', models.CharField(blank=True, db_column='cog_Esfera', max_length=1, null=True)),
                ('cog_programa', models.CharField(blank=True, db_column='cog_Programa', max_length=21, null=True)),
                ('cog_naturezadespesa', models.CharField(blank=True, db_column='cog_NaturezaDespesa', max_length=8, null=True)),
                ('cog_fonte', models.CharField(blank=True, db_column='cog_Fonte', max_length=9, null=True)),
                ('cog_identificadoruso', models.CharField(blank=True, db_column='cog_IdentificadorUso', max_length=4, null=True)),
                ('cog_lei', models.DecimalField(blank=True, db_column='cog_lei', decimal_places=2, max_digits=15, null=True)),
                ('cog_alteracao', models.DecimalField(blank=True, db_column='cog_Alteracao', decimal_places=2, max_digits=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'Créditos Orçamentários',
                'db_table': 'tbl_gdfcreditosorcamentarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='viw_gdfplanointerno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viw_codigodemanda', models.IntegerField(db_column='viw_CodigoDemanda', verbose_name='Demanda')),
                ('viw_coordenadorsetorial', models.CharField(db_collation='utf8mb4_general_ci', db_column='viw_CoordenadorSetorial', max_length=255, verbose_name='Coordenador Setorial')),
                ('viw_descricao', models.CharField(db_column='viw_Descricao', max_length=1000, verbose_name='Descrição')),
                ('viw_despesadetalhada', models.IntegerField(db_column='viw_DespesaDetalhada', verbose_name='Despesa Detalhada')),
                ('viw_previsão', models.DecimalField(db_column='viw_Previsao', decimal_places=2, max_digits=15, verbose_name='Previsão')),
                ('viw_empenhado', models.DecimalField(db_column='viw_ValorEmpenho', decimal_places=2, max_digits=15, verbose_name='Empenho')),
                ('viw_exercicioempenho', models.TextField(db_column='viw_ExercicioEmpenho', verbose_name='Exercício do Empenho')),
                ('viw_pioexercicio', models.TextField(db_column='viw_PioExercicio', verbose_name='Exercicio PIO')),
            ],
            options={
                'verbose_name_plural': 'Plano Interno de Orçamento',
                'db_table': 'viw_gdfplanointerno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblStatus',
            fields=[
                ('id_status', models.IntegerField(db_column='id_Status', primary_key=True, serialize=False)),
                ('sta_descricao', models.CharField(db_column='sta_descricao', max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Status',
                'db_table': 'tbl_status',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='tblcadastrodemandas',
            options={'managed': False, 'verbose_name_plural': 'Cadastro de Demandas'},
        ),
        migrations.AlterModelOptions(
            name='tblcoordenadoressetoriais',
            options={'managed': False, 'verbose_name_plural': 'Coordenadores Setoriais'},
        ),
        migrations.AlterModelOptions(
            name='tbldisponibilidade',
            options={'managed': False, 'verbose_name_plural': 'Disponibilidade'},
        ),
        migrations.AlterModelOptions(
            name='tblespeciedisponibilidade',
            options={'managed': False, 'verbose_name_plural': 'Especie de Disponibilidade'},
        ),
        migrations.AlterModelOptions(
            name='tblfcdfempenho',
            options={'managed': False, 'verbose_name_plural': 'Empenhos SIAFI'},
        ),
        migrations.AlterModelOptions(
            name='tblfcdfitemempenho',
            options={'managed': False, 'verbose_name_plural': 'Item de Empenho SIAFI'},
        ),
        migrations.AlterModelOptions(
            name='tblfcdfnaturezadespesadetalhada',
            options={'managed': False, 'verbose_name_plural': 'FCDF - Natureza da Despesa Detalhada'},
        ),
        migrations.AlterModelOptions(
            name='tblfcdfplanointernoorcamento',
            options={'managed': False, 'verbose_name_plural': 'Plano Interno de Orcamento - FCDF'},
        ),
        migrations.AlterModelOptions(
            name='tblfcdfremanejamento',
            options={'managed': False, 'verbose_name_plural': 'Remanejamentos - FCDF'},
        ),
        migrations.AlterModelOptions(
            name='tblgdfempenho',
            options={'managed': False, 'verbose_name_plural': 'Empenhos GDF'},
        ),
        migrations.AlterModelOptions(
            name='tblgdfnaturezadespesadetalhada',
            options={'managed': False, 'verbose_name_plural': 'Natureza da Despesa Detalhada - GDF'},
        ),
        migrations.AlterModelOptions(
            name='tblgdfpiocreditosorcamentarios',
            options={'managed': False, 'verbose_name_plural': 'Alocação de Créditos - GDF'},
        ),
        migrations.AlterModelOptions(
            name='tblgdfplanointernoorcamento',
            options={'managed': False, 'verbose_name_plural': 'Plano Interno de Orçamento - GDF'},
        ),
        migrations.AlterModelOptions(
            name='tblitemaquisicaoservico',
            options={'managed': False, 'verbose_name_plural': 'Item de Aquisição ou Serviço'},
        ),
        migrations.AlterModelOptions(
            name='tblperiodicidade',
            options={'managed': False, 'verbose_name_plural': 'Periodicidade'},
        ),
        migrations.AlterModelOptions(
            name='tblprevisaofaseexecucao',
            options={'managed': False, 'verbose_name_plural': 'Fase de Aquisicao'},
        ),
        migrations.AlterModelOptions(
            name='tblprocessoaquisicaoservico',
            options={'managed': False, 'verbose_name_plural': 'Processos de Aquisição e Contratação de Serviços'},
        ),
        migrations.AlterModelOptions(
            name='tblprodutounidade',
            options={'managed': False, 'verbose_name_plural': 'Produto/Unidade'},
        ),
    ]
