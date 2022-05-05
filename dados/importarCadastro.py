import pandas as pd
import datetime
import pymysql
import sqlalchemy

connect = sqlalchemy.create_engine('mysql+pymysql://root:DataSc1ence@localhost:3306/siorf')
df = pd.read_sql('tbl_cadastrodemandas', connect )

#dfLimpo = df.dropna(axis = 0)

#cadastroFcdf = df[['pif_CadastroDemanda', 'pif_Justificativa', 'pif_Fonte', 'pif_ProgramaTrabalho', 'pif_Quantidade', 'pif_Exercicio', 'pif_Observacao', 'pif_Data' ]]
#qddFcdf.insert(0,"DataEmissao", datetime.date.today())
#qddFcdf.columns = ["qdf_DataEmissao", "qdf_ExercicioFinanceiro", "qdf_Funcao", "qdf_Subfuncao", "qdf_Programa", "qdf_Acao", "qdf_Subtitulo", "qdf_PlanoOrcamentario", "qdf_Fonte", "qdf_NaturezaDespesa", "qdf_Lei", "qdf_DotacaoInicial", "qdf_DotacaoAtual", "qdf_Empenhado", "qdf_Liquidado", "qdf_Pago"]
connect2 = sqlalchemy.create_engine('mysql+pymysql://root:DataSc1ence@localhost:3306/siof')
df.to_sql('tbl_cadastrodemandas', connect2, index=False, if_exists='append')