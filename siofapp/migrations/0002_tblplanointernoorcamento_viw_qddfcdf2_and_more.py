# Generated by Django 4.0.3 on 2022-05-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siofapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblPlanointernoorcamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_fcdfplanointerno', models.BigIntegerField(blank=True, db_column='Id_FCDFPlanoInterno', null=True)),
                ('pif_cadastrodemandas', models.BigIntegerField(blank=True, db_column='pif_CadastroDemandas', null=True)),
                ('pif_justificativa', models.TextField(blank=True, db_column='pif_Justificativa', null=True)),
                ('pif_iniciativaestrategica', models.FloatField(blank=True, db_column='pif_IniciativaEstrategica', null=True)),
                ('pif_fonte', models.TextField(blank=True, db_column='pif_Fonte', null=True)),
                ('pif_funcao', models.TextField(blank=True, db_column='pif_Funcao', null=True)),
                ('pif_subfuncao', models.TextField(blank=True, db_column='pif_Subfuncao', null=True)),
                ('pif_programa', models.TextField(blank=True, db_column='pif_Programa', null=True)),
                ('pif_acao', models.TextField(blank=True, db_column='pif_Acao', null=True)),
                ('pif_subtitulo', models.TextField(blank=True, db_column='pif_Subtitulo', null=True)),
                ('pif_quantidade', models.BigIntegerField(blank=True, db_column='pif_Quantidade', null=True)),
                ('pif_valor', models.FloatField(blank=True, db_column='pif_Valor', null=True)),
                ('pif_exercicio', models.BigIntegerField(blank=True, db_column='pif_Exercicio', null=True)),
                ('pif_observacao', models.TextField(blank=True, db_column='pif_Observacao', null=True)),
                ('pif_data', models.DateTimeField(blank=True, db_column='pif_Data', null=True)),
            ],
            options={
                'db_table': 'tbl_planointernoorcamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='viw_qddfcdf2',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Emissao', models.DateField(db_column='Emissão')),
                ('Ano', models.TextField(db_column='Ano')),
                ('Ordenador', models.CharField(blank=True, db_column='Ordenador de Despesa', max_length=36, null=True)),
                ('Programa', models.CharField(blank=True, db_column='Programa de Trabalho', max_length=21, null=True)),
                ('Plano', models.CharField(blank=True, db_column='Plano Orcamentário', max_length=144, null=True)),
                ('Fonte', models.CharField(blank=True, db_column='Fonte', max_length=3, null=True)),
                ('Grupo', models.CharField(blank=True, db_column='Grupo de Despesa', max_length=25, null=True)),
                ('Lei', models.DecimalField(blank=True, db_column='Lei', decimal_places=2, max_digits=37, null=True)),
                ('DotacaoInicial', models.DecimalField(blank=True, db_column='Dotação Inicial', decimal_places=2, max_digits=38, null=True)),
                ('DotacaoAtual', models.DecimalField(blank=True, db_column='Dotação Atual', decimal_places=2, max_digits=38, null=True)),
                ('Empenhado', models.DecimalField(blank=True, db_column='Empenhado', decimal_places=2, max_digits=37, null=True)),
                ('Liquidado', models.DecimalField(blank=True, db_column='Liquidado', decimal_places=2, max_digits=37, null=True)),
                ('Pago', models.DecimalField(blank=True, db_column='Pago', decimal_places=2, max_digits=37, null=True)),
            ],
            options={
                'db_table': 'viw_qddfcdf2',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='viw_fcdfqdd2',
        ),
    ]
