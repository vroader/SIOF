# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TblAlinhamentoestrategico(models.Model):
    id_alinhamentoestrategico = models.IntegerField(db_column='Id_AlinhamentoEstrategico', primary_key=True)  # Field name made lowercase.
    ale_processoaquisicaoservico = models.ForeignKey('TblProcessoaquisicaoservico', models.DO_NOTHING, db_column='ale_ProcessoAquisicaoServico')  # Field name made lowercase.
    ale_iniciativaestrategica = models.ForeignKey('TblIniciativaestrategica', models.DO_NOTHING, db_column='ale_IniciativaEstrategica')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_alinhamentoestrategico'


class TblCadastrodemandas(models.Model):
    id_cadastrodemandas = models.AutoField(db_column='Id_CadastroDemandas', primary_key=True)  # Field name made lowercase.
    cad_codigodemanda = models.IntegerField(db_column='cad_CodigoDemanda')  # Field name made lowercase.
    cad_coordenadorsetorial = models.ForeignKey('TblCoordenadoressetoriais', models.DO_NOTHING, db_column='cad_CoordenadorSetorial')  # Field name made lowercase.
    cad_descricao = models.CharField(db_column='cad_Descricao', max_length=255, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    cad_fcdfdespesadetalhada = models.ForeignKey('TblFcdfnaturezadespesadetalhada', models.DO_NOTHING, db_column='cad_FCDFDespesaDetalhada', blank=True, null=True)  # Field name made lowercase.
    cad_gdfdespesadetalhada = models.ForeignKey('TblGdfnaturezadespesadetalhada', models.DO_NOTHING, db_column='cad_GDFDespesaDetalhada', blank=True, null=True)  # Field name made lowercase.
    cad_produtounidade = models.ForeignKey('TblProdutounidade', models.DO_NOTHING, db_column='cad_ProdutoUnidade', blank=True, null=True)  # Field name made lowercase.
    cad_periodicidade = models.ForeignKey('TblPeriodicidade', models.DO_NOTHING, db_column='cad_Periodicidade', blank=True, null=True)  # Field name made lowercase.
    cad_especiedisponibilidade = models.ForeignKey('TblEspeciedisponibilidade', models.DO_NOTHING, db_column='cad_EspecieDisponibilidade', blank=True, null=True)  # Field name made lowercase.
    cad_observacao = models.CharField(db_column='cad_Observacao', max_length=1000, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.
    cad_datainclusao = models.DateField(db_column='cad_DataInclusao', blank=True, null=True)  # Field name made lowercase.
    cad_status = models.IntegerField(db_column='cad_Status', blank=True, null=True)  # Field name made lowercase.
    cad_especiedespesa = models.CharField(db_column='cad_EspecieDespesa', max_length=2500, db_collation='utf8mb4_general_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cadastrodemandas'


class TblCoordenadoressetoriais(models.Model):
    cso_codigo = models.CharField(db_column='cso_Codigo', primary_key=True, max_length=8)  # Field name made lowercase.
    cso_nome = models.CharField(db_column='cso_Nome', max_length=255)  # Field name made lowercase.
    cso_areatematica = models.CharField(db_column='cso_AreaTematica', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cso_datainclusao = models.DateField(db_column='cso_DataInclusao', blank=True, null=True)  # Field name made lowercase.
    cso_status = models.IntegerField(db_column='cso_Status', blank=True, null=True)  # Field name made lowercase.
    cso_instrumentolegal = models.CharField(db_column='cso_InstrumentoLegal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cso_ordenadordespesa = models.CharField(db_column='cso_OrdenadorDespesa', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_coordenadoressetoriais'


class TblDisponibilidade(models.Model):
    id_disponibilidade = models.AutoField(db_column='Id_Disponibilidade', primary_key=True)  # Field name made lowercase.
    dsp_status = models.CharField(db_column='dsp_Status', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_disponibilidade'


class TblEspeciedisponibilidade(models.Model):
    id_especiedisponibilidade = models.AutoField(db_column='Id_EspecieDisponibilidade', primary_key=True)  # Field name made lowercase.
    esd_disponibilidade = models.ForeignKey(TblDisponibilidade, models.DO_NOTHING, db_column='esd_Disponibilidade')  # Field name made lowercase.
    esd_discriminacao = models.CharField(db_column='esd_Discriminacao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_especiedisponibilidade'


class TblEstrategia(models.Model):
    id_estrategia = models.AutoField(db_column='Id_Estrategia', primary_key=True)  # Field name made lowercase.
    est_codigo = models.CharField(db_column='est_Codigo', max_length=6)  # Field name made lowercase.
    est_objetivo = models.ForeignKey('TblObjetivo', models.DO_NOTHING, db_column='est_Objetivo')  # Field name made lowercase.
    est_descricao = models.CharField(db_column='est_Descricao', max_length=250)  # Field name made lowercase.
    est_status = models.IntegerField(db_column='est_Status', blank=True, null=True)  # Field name made lowercase.
    est_observacao = models.CharField(db_column='est_Observacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_estrategia'


class TblFcdfcreditosorcamentarios(models.Model):
    id_fcdfcreditosorcamentarios = models.IntegerField(db_column='Id_FCDFCreditosOrcamentarios', primary_key=True)  # Field name made lowercase.
    cof_fcdfplanointernoorcamento = models.ForeignKey('TblFcdfplanointernoorcamento', models.DO_NOTHING, db_column='cof_FCDFPlanoInternoOrcamento')  # Field name made lowercase.
    cof_fcdfquadrodetalhamentodespesa = models.ForeignKey('TblFcdfquadrodetalhamentodespesa', models.DO_NOTHING, db_column='cof_FCDFQuadroDetalhamentoDespesa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfcreditosorcamentarios'


class TblFcdfempenho(models.Model):
    emf_codigo = models.CharField(db_column='emf_Codigo', primary_key=True, max_length=23)  # Field name made lowercase.
    emf_descricao = models.CharField(db_column='emf_Descricao', max_length=1000)  # Field name made lowercase.
    emf_numeroprocesso = models.CharField(db_column='emf_NumeroProcesso', max_length=23, blank=True, null=True)  # Field name made lowercase.
    emf_dataemissao = models.DateField(db_column='emf_DataEmissao', blank=True, null=True)  # Field name made lowercase.
    emf_esfera = models.CharField(db_column='emf_Esfera', max_length=23, blank=True, null=True)  # Field name made lowercase.
    emf_fonte = models.CharField(db_column='emf_Fonte', max_length=10, blank=True, null=True)  # Field name made lowercase.
    emf_programatrabalhoresumido = models.CharField(db_column='emf_ProgramaTrabalhoResumido', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfempenho'


class TblFcdfitemempenho(models.Model):
    id_fcdfitemempenho = models.AutoField(db_column='Id_FCDFItemEmpenho', primary_key=True)  # Field name made lowercase.
    ias_itemaquisicaoservico = models.ForeignKey('TblItemaquisicaoservico', models.DO_NOTHING, db_column='ias_ItemAquisicaoServico')  # Field name made lowercase.
    itf_empenho = models.ForeignKey(TblFcdfempenho, models.DO_NOTHING, db_column='itf_Empenho')  # Field name made lowercase.
    itf_descricao = models.CharField(db_column='itf_Descricao', max_length=100)  # Field name made lowercase.
    itf_operacao = models.CharField(db_column='itf_Operacao', max_length=50)  # Field name made lowercase.
    itf_quantidade = models.DecimalField(db_column='itf_Quantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itf_valor = models.DecimalField(db_column='itf_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itf_data = models.DateField(db_column='itf_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfitemempenho'


class TblFcdfitemliquidacao(models.Model):
    id_fcdfitemliquidacao = models.IntegerField(db_column='Id_FCDFItemLiquidacao', primary_key=True)  # Field name made lowercase.
    lig_fcdfitemempenho = models.ForeignKey(TblFcdfitemempenho, models.DO_NOTHING, db_column='lig_FCDFItemEmpenho')  # Field name made lowercase.
    lig_quantidade = models.DecimalField(db_column='lig_Quantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lig_valor = models.DecimalField(db_column='lig_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfitemliquidacao'


class TblFcdfitempagamento(models.Model):
    id_fcdfitempagamento = models.IntegerField(db_column='Id_FCDFItemPagamento', primary_key=True)  # Field name made lowercase.
    pgf_fcdfitemliquidacao = models.ForeignKey(TblFcdfitemliquidacao, models.DO_NOTHING, db_column='pgf_FCDFItemLiquidacao')  # Field name made lowercase.
    pgf_quantidade = models.DecimalField(db_column='pgf_Quantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pgf_vavlor = models.DecimalField(db_column='pgf_Vavlor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pgf_data = models.DateField(db_column='pgf_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfitempagamento'


class TblFcdfnaturezadespesadetalhada(models.Model):
    nfc_codigo = models.CharField(db_column='nfc_Codigo', primary_key=True, max_length=8)  # Field name made lowercase.
    nfc_descricao = models.CharField(db_column='nfc_Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nfc_categoriaeconomica = models.CharField(db_column='nfc_CategoriaEconomica', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nfc_grupodespesa = models.CharField(db_column='nfc_GrupoDespesa', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nfc_modalidadeaplicacao = models.CharField(db_column='nfc_ModalidadeAplicacao', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nfc_elementodespesa = models.CharField(db_column='nfc_ElementoDespesa', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfnaturezadespesadetalhada'


class TblFcdfplanointernoorcamento(models.Model):
    id_fcdfplanointerno = models.AutoField(db_column='Id_FCDFPlanoInterno', primary_key=True)  # Field name made lowercase.
    pif_cadastrodemanda = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='pif_CadastroDemanda')  # Field name made lowercase.
    pif_justificativa = models.CharField(db_column='pif_Justificativa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pif_fonte = models.CharField(db_column='pif_Fonte', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pif_programatrabalho = models.CharField(db_column='pif_ProgramaTrabalho', max_length=21, blank=True, null=True)  # Field name made lowercase.
    pif_quantidade = models.IntegerField(db_column='pif_Quantidade', blank=True, null=True)  # Field name made lowercase.
    pif_valor = models.DecimalField(db_column='pif_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pif_exercicio = models.TextField(db_column='pif_Exercicio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pif_observacao = models.CharField(db_column='pif_Observacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pif_data = models.DateField(db_column='pif_Data')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfplanointernoorcamento'


class TblFcdfproposta(models.Model):
    id_fcdfproposta = models.AutoField(db_column='Id_FCDFProposta', primary_key=True)  # Field name made lowercase.
    prf_cadastrodemanda = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='prf_CadastroDemanda')  # Field name made lowercase.
    prf_justificativa = models.CharField(db_column='prf_Justificativa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prf_quantidade = models.IntegerField(db_column='prf_Quantidade', blank=True, null=True)  # Field name made lowercase.
    prf_valor = models.DecimalField(db_column='prf_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prf_fonte = models.CharField(db_column='prf_Fonte', max_length=3, blank=True, null=True)  # Field name made lowercase.
    prf_programatrabalho = models.CharField(db_column='prf_ProgramaTrabalho', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prf_exercicio = models.TextField(db_column='prf_Exercicio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfproposta'


class TblFcdfquadrodetalhamentodespesa(models.Model):
    id_gdfquadrodetalhamentodespesa = models.AutoField(db_column='id_GDFQuadroDetalhamentoDespesa', primary_key=True)  # Field name made lowercase.
    qdf_dataemissao = models.DateField(db_column='qdf_DataEmissao', blank=True, null=True)  # Field name made lowercase.
    qdf_exerciciofinanceiro = models.TextField(db_column='qdf_ExercicioFinanceiro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qdf_funcao = models.CharField(db_column='qdf_Funcao', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_subfuncao = models.CharField(db_column='qdf_Subfuncao', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_programa = models.CharField(db_column='qdf_Programa', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_acao = models.CharField(db_column='qdf_Acao', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_subtitulo = models.CharField(db_column='qdf_Subtitulo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_planoorcamentario = models.CharField(db_column='qdf_PlanoOrcamentario', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_fonte = models.CharField(db_column='qdf_Fonte', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_naturezadespesa = models.CharField(db_column='qdf_NaturezaDespesa', max_length=150, blank=True, null=True)  # Field name made lowercase.
    qdf_lei = models.DecimalField(db_column='qdf_Lei', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdf_dotacaoinicial = models.DecimalField(db_column='qdf_DotacaoInicial', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdf_dotacaoatual = models.DecimalField(db_column='qdf_DotacaoAtual', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdf_empenhado = models.DecimalField(db_column='qdf_Empenhado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdf_liquidado = models.DecimalField(db_column='qdf_Liquidado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdf_pago = models.DecimalField(db_column='qdf_Pago', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfquadrodetalhamentodespesa'


class TblFcdfremanejamento(models.Model):
    id_fcdfremanejamentos = models.AutoField(db_column='Id_FCDFRemanejamentos', primary_key=True)  # Field name made lowercase.
    ref_planointerno = models.ForeignKey(TblFcdfplanointernoorcamento, models.DO_NOTHING, db_column='ref_PlanoInterno')  # Field name made lowercase.
    ref_descricao = models.CharField(db_column='ref_Descricao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    ref_especieremanejamento = models.CharField(db_column='ref_EspecieRemanejamento', max_length=13)  # Field name made lowercase.
    ref_quantidade = models.IntegerField(db_column='ref_Quantidade', blank=True, null=True)  # Field name made lowercase.
    ref_valor = models.DecimalField(db_column='ref_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ref_data = models.DateField(db_column='ref_Data')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fcdfremanejamento'


class TblGdfempenho(models.Model):
    emg_codigo = models.CharField(db_column='emg_Codigo', primary_key=True, max_length=23)  # Field name made lowercase.
    emg_descricao = models.CharField(db_column='emg_Descricao', max_length=1000)  # Field name made lowercase.
    emf_numeroprocesso = models.CharField(db_column='emf_NumeroProcesso', max_length=23, blank=True, null=True)  # Field name made lowercase.
    emf_dataemissao = models.DateField(db_column='emf_DataEmissao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfempenho'


class TblGdfitemempenho(models.Model):
    id_gdfitemempenho = models.AutoField(db_column='Id_GDFItemEmpenho', primary_key=True)  # Field name made lowercase.
    ias_itemaquisicaoservico = models.ForeignKey('TblItemaquisicaoservico', models.DO_NOTHING, db_column='ias_ItemAquisicaoServico')  # Field name made lowercase.
    itf_descricao = models.CharField(db_column='itf_Descricao', max_length=100)  # Field name made lowercase.
    itf_operacao = models.CharField(db_column='itf_Operacao', max_length=50)  # Field name made lowercase.
    itf_quantidade = models.DecimalField(db_column='itf_Quantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itg_valor = models.DecimalField(db_column='itg_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    itg_data = models.DateField(db_column='itg_Data', blank=True, null=True)  # Field name made lowercase.
    itg_gdfempenho = models.ForeignKey(TblGdfempenho, models.DO_NOTHING, db_column='itg_GDFEmpenho')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfitemempenho'


class TblGdfitemliquidacao(models.Model):
    id_gdfitemliquidacao = models.IntegerField(db_column='Id_GDFItemLiquidacao', primary_key=True)  # Field name made lowercase.
    lig_gdfitemempenho = models.ForeignKey(TblGdfitemempenho, models.DO_NOTHING, db_column='lig_GDFItemEmpenho')  # Field name made lowercase.
    lig_qantidade = models.DecimalField(db_column='lig_Qantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lig_valor = models.DecimalField(db_column='lig_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfitemliquidacao'


class TblGdfitempagamento(models.Model):
    id_gdfitempagamento = models.IntegerField(db_column='Id_GDFItemPagamento', primary_key=True)  # Field name made lowercase.
    pag_gdfitemliquidacao = models.ForeignKey(TblGdfitemliquidacao, models.DO_NOTHING, db_column='pag_GDFItemLiquidacao')  # Field name made lowercase.
    pag_qantidade = models.DecimalField(db_column='pag_Qantidade', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pag_valor = models.DecimalField(db_column='pag_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfitempagamento'


class TblGdfnaturezadespesadetalhada(models.Model):
    ndf_codigo = models.CharField(db_column='ndf_Codigo', primary_key=True, max_length=8)  # Field name made lowercase.
    ndf_descricao = models.CharField(db_column='ndf_Descricao', max_length=255)  # Field name made lowercase.
    ndf_categoriaeconomica = models.CharField(db_column='ndf_CategoriaEconomica', max_length=3)  # Field name made lowercase.
    ndf_grupodespesa = models.CharField(db_column='ndf_GrupoDespesa', max_length=3)  # Field name made lowercase.
    ndf_modalidadeaplicacao = models.CharField(db_column='ndf_ModalidadeAplicacao', max_length=2)  # Field name made lowercase.
    ndf_elementodespesa = models.CharField(db_column='ndf_ElementoDespesa', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfnaturezadespesadetalhada'


class TblGdfpiocreditosorcamentarios(models.Model):
    id_gdfpiocreditosorcamentarios = models.IntegerField(db_column='Id_GDFPIOCreditosOrcamentarios', primary_key=True)  # Field name made lowercase.
    cog_gdfplanointernoorcamento = models.ForeignKey('TblGdfplanointernoorcamento', models.DO_NOTHING, db_column='cog_GDFPlanoInternoOrcamento')  # Field name made lowercase.
    cog_gdfquadrodetalhamentodespesa = models.ForeignKey('TblGdfquadrodetalhamentodespesa', models.DO_NOTHING, db_column='cog_GDFQuadroDetalhamentoDespesa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfpiocreditosorcamentarios'


class TblGdfplanointernoorcamento(models.Model):
    id_gdfplanointernoorcamento = models.AutoField(db_column='Id_GDFPlanoInternoOrcamento', primary_key=True)  # Field name made lowercase.
    pig_cadastrodemanda = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='pig_CadastroDemanda')  # Field name made lowercase.
    pig_quantidade = models.IntegerField(db_column='pig_Quantidade', blank=True, null=True)  # Field name made lowercase.
    pig_valor = models.DecimalField(db_column='pig_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pig_data = models.DateField(db_column='pig_Data')  # Field name made lowercase.
    pig_observacoes = models.CharField(db_column='pig_Observacoes', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfplanointernoorcamento'


class TblGdfproposta(models.Model):
    id_gdfproposta = models.AutoField(db_column='Id_GDFProposta', primary_key=True)  # Field name made lowercase.
    prg_cadastrodemada = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='prg_CadastroDemada')  # Field name made lowercase.
    prg_justificativa = models.CharField(db_column='prg_Justificativa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prg_quantidade = models.IntegerField(db_column='prg_Quantidade', blank=True, null=True)  # Field name made lowercase.
    prg_valor = models.DecimalField(db_column='prg_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    prg_unidadeorcamentaria = models.CharField(db_column='prg_UnidadeOrcamentaria', max_length=5, blank=True, null=True)  # Field name made lowercase.
    prg_fonte = models.CharField(db_column='prg_Fonte', max_length=9, blank=True, null=True)  # Field name made lowercase.
    prg_identificadoruso = models.IntegerField(db_column='prg_IdentificadorUso', blank=True, null=True)  # Field name made lowercase.
    prg_programatrabalho = models.CharField(db_column='prg_ProgramaTrabalho', max_length=17, blank=True, null=True)  # Field name made lowercase.
    prg_exercicio = models.TextField(db_column='prg_Exercicio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tbl_gdfproposta'


class TblGdfquadrodetalhamentodespesa(models.Model):
    id_gdfquadrodetalhamentodespesa = models.AutoField(db_column='id_GDFQuadroDetalhamentoDespesa', primary_key=True)  # Field name made lowercase.
    qdg_exerciciofinanceiro = models.TextField(db_column='qdg_ExercicioFinanceiro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qdg_unidadeorcamentaria = models.IntegerField(db_column='qdg_UnidadeOrcamentaria', blank=True, null=True)  # Field name made lowercase.
    qdg_mesreferencia = models.CharField(db_column='qdg_MesReferencia', max_length=11, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    qdg_dataemissao = models.DateField(db_column='qdg_DataEmissao', blank=True, null=True)  # Field name made lowercase.
    qdg_esfera = models.IntegerField(db_column='qdg_Esfera', blank=True, null=True)  # Field name made lowercase.
    qdg_naturezadespesa = models.IntegerField(db_column='qdg_NaturezaDespesa', blank=True, null=True)  # Field name made lowercase.
    qdg_fonte = models.IntegerField(db_column='qdg_Fonte', blank=True, null=True)  # Field name made lowercase.
    qdg_identificadoruso = models.IntegerField(db_column='qdg_IdentificadorUso', blank=True, null=True)  # Field name made lowercase.
    qdg_programatrabalho = models.CharField(db_column='qdg_ProgramaTrabalho', max_length=17, blank=True, null=True)  # Field name made lowercase.
    qdg_lei = models.DecimalField(db_column='qdg_Lei', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_alteracao = models.DecimalField(db_column='qdg_Alteracao', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_contingenciado = models.DecimalField(db_column='qdg_Contingenciado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_cota = models.DecimalField(db_column='qdg_Cota', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_bloqueado = models.DecimalField(db_column='qdg_Bloqueado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_despesaautorizada = models.DecimalField(db_column='qdg_DespesaAutorizada', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_empenhado = models.DecimalField(db_column='qdg_Empenhado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_disponivel = models.DecimalField(db_column='qdg_Disponivel', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    qdg_liquidado = models.DecimalField(db_column='qdg_Liquidado', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfquadrodetalhamentodespesa'


class TblGdfremanejamento(models.Model):
    id_gdfremanejamentos = models.AutoField(db_column='Id_GDFRemanejamentos', primary_key=True)  # Field name made lowercase.
    reg_descricao = models.CharField(db_column='reg_Descricao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_especieremanejamento = models.CharField(db_column='reg_EspecieRemanejamento', max_length=13)  # Field name made lowercase.
    reg_quantidade = models.IntegerField(db_column='reg_Quantidade', blank=True, null=True)  # Field name made lowercase.
    reg_valor = models.DecimalField(db_column='reg_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reg_data = models.DateField(db_column='reg_Data')  # Field name made lowercase.
    reg_planointerno = models.ForeignKey(TblGdfplanointernoorcamento, models.DO_NOTHING, db_column='reg_PlanoInterno')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_gdfremanejamento'


class TblIniciativaestrategica(models.Model):
    id_iniciativaestrategica = models.AutoField(db_column='Id_IniciativaEstrategica', primary_key=True)  # Field name made lowercase.
    ini_codigo = models.CharField(db_column='ini_Codigo', max_length=9)  # Field name made lowercase.
    ini_estrategia = models.ForeignKey(TblEstrategia, models.DO_NOTHING, db_column='ini_Estrategia')  # Field name made lowercase.
    ini_descricao = models.CharField(db_column='ini_Descricao', max_length=250)  # Field name made lowercase.
    ini_status = models.IntegerField(db_column='ini_Status', blank=True, null=True)  # Field name made lowercase.
    ini_observacao = models.CharField(db_column='ini_Observacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_iniciativaestrategica'


class TblItemaquisicaoservico(models.Model):
    id_itemaqusicaoservico = models.IntegerField(db_column='Id_ItemAqusicaoServico', primary_key=True)  # Field name made lowercase.
    ias_processoaqusicaoservico = models.ForeignKey('TblProcessoaquisicaoservico', models.DO_NOTHING, db_column='ias_ProcessoAqusicaoServico')  # Field name made lowercase.
    ias_codigo = models.IntegerField(db_column='ias_Codigo', blank=True, null=True)  # Field name made lowercase.
    ias_descricao = models.CharField(db_column='ias_Descricao', max_length=500, blank=True, null=True)  # Field name made lowercase.
    ias_quantidade = models.IntegerField(db_column='ias_Quantidade', blank=True, null=True)  # Field name made lowercase.
    ias_unidademedida = models.CharField(db_column='ias_UnidadeMedida', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ias_valor = models.DecimalField(db_column='ias_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ias_cadastrodemanda = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='ias_CadastroDemanda')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_itemaquisicaoservico'


class TblObjetivo(models.Model):
    id_objetivo = models.AutoField(db_column='Id_Objetivo', primary_key=True)  # Field name made lowercase.
    obj_codigo = models.CharField(db_column='obj_Codigo', max_length=3)  # Field name made lowercase.
    obj_descricao = models.CharField(db_column='obj_Descricao', max_length=250)  # Field name made lowercase.
    obj_status = models.IntegerField(db_column='obj_Status', blank=True, null=True)  # Field name made lowercase.
    obj_observacao = models.CharField(db_column='obj_Observacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_objetivo'


class TblPeriodicidade(models.Model):
    id_periodicidade = models.IntegerField(db_column='Id_Periodicidade', primary_key=True)  # Field name made lowercase.
    per_descricao = models.CharField(db_column='per_Descricao', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_periodicidade'


class TblPlanointernoorcamento(models.Model):
    id_fcdfplanointerno = models.BigIntegerField(db_column='Id_FCDFPlanoInterno', blank=True, null=True)  # Field name made lowercase.
    pif_cadastrodemandas = models.BigIntegerField(db_column='pif_CadastroDemandas', blank=True, null=True)  # Field name made lowercase.
    pif_justificativa = models.TextField(db_column='pif_Justificativa', blank=True, null=True)  # Field name made lowercase.
    pif_iniciativaestrategica = models.FloatField(db_column='pif_IniciativaEstrategica', blank=True, null=True)  # Field name made lowercase.
    pif_fonte = models.TextField(db_column='pif_Fonte', blank=True, null=True)  # Field name made lowercase.
    pif_funcao = models.TextField(db_column='pif_Funcao', blank=True, null=True)  # Field name made lowercase.
    pif_subfuncao = models.TextField(db_column='pif_Subfuncao', blank=True, null=True)  # Field name made lowercase.
    pif_programa = models.TextField(db_column='pif_Programa', blank=True, null=True)  # Field name made lowercase.
    pif_acao = models.TextField(db_column='pif_Acao', blank=True, null=True)  # Field name made lowercase.
    pif_subtitulo = models.TextField(db_column='pif_Subtitulo', blank=True, null=True)  # Field name made lowercase.
    pif_quantidade = models.BigIntegerField(db_column='pif_Quantidade', blank=True, null=True)  # Field name made lowercase.
    pif_valor = models.FloatField(db_column='pif_Valor', blank=True, null=True)  # Field name made lowercase.
    pif_exercicio = models.BigIntegerField(db_column='pif_Exercicio', blank=True, null=True)  # Field name made lowercase.
    pif_observacao = models.TextField(db_column='pif_Observacao', blank=True, null=True)  # Field name made lowercase.
    pif_data = models.DateTimeField(db_column='pif_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_planointernoorcamento'


class TblPrevisaofaseexecucao(models.Model):
    id_previsaofaseexecucao = models.IntegerField(db_column='Id_PrevisaoFaseExecucao', primary_key=True)  # Field name made lowercase.
    fse_fase = models.CharField(db_column='fse_Fase', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fse_inicio = models.DateField(db_column='fse_Inicio', blank=True, null=True)  # Field name made lowercase.
    fse_termino = models.DateField(db_column='fse_Termino', blank=True, null=True)  # Field name made lowercase.
    fse_processoaquisicaoservico = models.ForeignKey('TblProcessoaquisicaoservico', models.DO_NOTHING, db_column='fse_ProcessoAquisicaoServico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_previsaofaseexecucao'


class TblProcessoaquisicaoservico(models.Model):
    id_processoaquisicaoservico = models.CharField(db_column='Id_ProcessoAquisicaoServico', primary_key=True, max_length=19)  # Field name made lowercase.
    pas_responsavel = models.CharField(db_column='pas_Responsavel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pas_descricao = models.CharField(db_column='pas_Descricao', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_processoaquisicaoservico'


class TblProdutounidade(models.Model):
    pdu_codigo = models.IntegerField(db_column='pdu_Codigo', primary_key=True)  # Field name made lowercase.
    pdu_especificacao = models.CharField(db_column='pdu_Especificacao', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pdu_unidademedida = models.CharField(db_column='pdu_UnidadeMedida', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_produtounidade'


class TblPropostasetorial(models.Model):
    id_propostasetorial = models.AutoField(db_column='Id_PropostaSetorial', primary_key=True)  # Field name made lowercase.
    pps_cadastrodemanda = models.ForeignKey(TblCadastrodemandas, models.DO_NOTHING, db_column='pps_CadastroDemanda')  # Field name made lowercase.
    pps_justificativa = models.CharField(db_column='pps_Justificativa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pps_quantidade = models.IntegerField(db_column='pps_Quantidade', blank=True, null=True)  # Field name made lowercase.
    pps_valor = models.DecimalField(db_column='pps_Valor', max_digits=15, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pps_observacao = models.CharField(db_column='pps_Observacao', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    pps_unidadedemandante = models.CharField(db_column='pps_UnidadeDemandante', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pps_exercicio = models.TextField(db_column='pps_Exercicio')  # Field name made lowercase. This field type is a guess.
    pps_status = models.IntegerField(db_column='pps_Status', blank=True, null=True)  # Field name made lowercase.
    pps_data = models.DateField(db_column='pps_Data')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_propostasetorial'

class viw_qddfcdf2(models.Model):
    id = models.BigIntegerField(primary_key=True)
    Emissao = models.DateField(db_column='Emissão')
    Ano = models.TextField(db_column='Ano')
    Ordenador= models.CharField(db_column='Ordenador de Despesa', max_length=36, blank=True, null=True)
    Programa= models.CharField(db_column='Programa de Trabalho', max_length=21, blank=True, null=True)
    Plano = models.CharField(db_column='Plano Orcamentário', max_length=144, blank=True, null=True)
    Fonte = models.CharField (db_column='Fonte', max_length=3, blank=True, null=True)
    Grupo = models.CharField(db_column='Grupo de Despesa', max_length=25, blank=True, null=True)
    Lei = models.DecimalField(db_column='Lei', max_digits=37, decimal_places=2, blank=True, null=True)
    DotacaoInicial =models.DecimalField(db_column='Dotação Inicial', max_digits=38, decimal_places=2, blank=True, null=True)
    DotacaoAtual = models.DecimalField(db_column='Dotação Atual', max_digits=38, decimal_places=2, blank=True, null=True)
    Empenhado = models.DecimalField(db_column='Empenhado', max_digits=37, decimal_places=2, blank=True, null=True)
    Liquidado = models.DecimalField(db_column='Liquidado', max_digits=37, decimal_places=2, blank=True, null=True)
    Pago = models.DecimalField(db_column='Pago', max_digits=37, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'viw_qddfcdf2'