import pandas as pd
import datetime
import pymysql
import sqlalchemy

df = pd.read_csv('tbl_fcdfplanointernoorcamento.csv')

#dfLimpo = df.dropna(axis = 0)

#pioFcdf = df[['pif_CadastroDemanda', 'pif_Justificativa', 'pif_Fonte', 'pif_ProgramaTrabalho', 'pif_Quantidade', 'pif_Exercicio', 'pif_Observacao', 'pif_Data' ]]
#qddFcdf.insert(0,"DataEmissao", datetime.date.today())
#qddFcdf.columns = ["qdf_DataEmissao", "qdf_ExercicioFinanceiro", "qdf_Funcao", "qdf_Subfuncao", "qdf_Programa", "qdf_Acao", "qdf_Subtitulo", "qdf_PlanoOrcamentario", "qdf_Fonte", "qdf_NaturezaDespesa", "qdf_Lei", "qdf_DotacaoInicial", "qdf_DotacaoAtual", "qdf_Empenhado", "qdf_Liquidado", "qdf_Pago"]
connect = sqlalchemy.create_engine('mysql+pymysql://root:DataSc1ence@localhost:3306/siof')
df.to_sql('tbl_fcdfplanointernoorcamento', connect, index=False, if_exists='append')