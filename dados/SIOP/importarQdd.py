import pandas as pd
import datetime
import pymysql
import sqlalchemy

df = pd.read_excel('85de9a73817b46da9eb0c681d87c686f.xlsx')

dfLimpo = df.dropna(axis = 0)

qddFcdf = dfLimpo[["Ano", "Função", "Subfunção", "Programa", "Ação", "Localizador", "Plano Orçamentário", "Fonte", "Natureza de Despesa", "Projeto de Lei", "Dotação Inicial", "Dotação Atual", "Empenhado", "Liquidado", "Pago" ]]
qddFcdf.insert(0,"DataEmissao", datetime.date.today())
qddFcdf.columns = ["qdf_DataEmissao", "qdf_ExercicioFinanceiro", "qdf_Funcao", "qdf_Subfuncao", "qdf_Programa", "qdf_Acao", "qdf_Subtitulo", "qdf_PlanoOrcamentario", "qdf_Fonte", "qdf_NaturezaDespesa", "qdf_Lei", "qdf_DotacaoInicial", "qdf_DotacaoAtual", "qdf_Empenhado", "qdf_Liquidado", "qdf_Pago"]
connect = sqlalchemy.create_engine('mysql+pymysql://root:DataSc1ence@localhost:3306/siof')
qddFcdf.to_sql('tbl_fcdfquadrodetalhamentodespesa', connect, index=False, if_exists='append')