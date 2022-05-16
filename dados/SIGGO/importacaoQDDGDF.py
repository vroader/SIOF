import csv
import re
import datetime
import sqlalchemy

def importarQDD (nomeTabela):
    tbl_QDDGDF = open(nomeTabela, encoding = 'latin-1')
    QDDGDF_Readeble = csv.reader(tbl_QDDGDF, delimiter=';')
    QDDGDF = list(QDDGDF_Readeble)
    return QDDGDF



lista = importarQDD('24904.csv')


exercicio = input("Informe o exercício fiscal:")
unidadeOrcamentaria = re.sub('Unidade Orçamentária: ','', lista[2][0])
mesReferencia = re.sub('Mês de Referência: ', '', lista[3][0])
emissao = re.search(r'\d{2}/\d{2}/\d{4}', lista[4][0]).group()
dataEmissao = datetime.datetime.strptime(emissao, "%d/%m/%Y").strftime("%Y-%m-%d")

listaQDDGDF = []
for linha in lista:
    fonteRecurso = []
    if re.match('Esfera',linha[0]):
        esfera = linha[1]
        programa = linha[4]         
    elif re.search(r'\d\d\d\d\d\d', linha[0]):
        fonteRecurso.append(exercicio)
        fonteRecurso.append(unidadeOrcamentaria)
        fonteRecurso.append(mesReferencia)
        fonteRecurso.append(dataEmissao)
        fonteRecurso.append(esfera)
        fonteRecurso.append(programa)
        fonteRecurso.append(linha[0])#insere a natureza da despesa
        fonteRecurso.append(linha[1])#insere a fonte de recurso
        fonteRecurso.append(linha[2])#insere o idUso
        fonteRecurso.append(linha[3].replace('.', '').replace(',', '.'))#insere a previsão na lei
        fonteRecurso.append(linha[4].replace('.', '').replace(',', '.'))#insere as alterações
        fonteRecurso.append(linha[5].replace('.', '').replace(',', '.'))#insere o contingenciamento
        fonteRecurso.append(linha[6].replace('.', '').replace(',', '.'))#insere a cota
        fonteRecurso.append(linha[7].replace('.', '').replace(',', '.'))#insere os Bloqueios
        fonteRecurso.append(linha[8].replace('.', '').replace(',', '.'))#insere a despesa autorizada
        fonteRecurso.append(linha[9].replace('.', '').replace(',', '.'))#insere o empenho
        fonteRecurso.append(linha[10].replace('.', '').replace(',', '.'))#insere o valor disponível
        fonteRecurso.append(linha[11].replace('.', '').replace(',', '.'))#insere o valor liquidado
        listaQDDGDF.append(fonteRecurso)
        
engine = sqlalchemy.create_engine('mysql+pymysql://root:DataSc1ence@localhost:3306/siof')
for registro in listaQDDGDF:
    engine.execute('INSERT INTO tbl_gdfquadrodetalhamentodespesa\
                   ( qdg_ExercicioFinanceiro,\
                    qdg_UnidadeOrcamentaria,\
                    qdg_MesReferencia,\
                    qdg_DataEmissao,\
                    qdg_Esfera,\
                    qdg_ProgramaTrabalho,\
                    qdg_NaturezaDespesa,\
                    qdg_Fonte,\
                    qdg_IdentificadorUso,\
                    qdg_Lei,\
                    qdg_Alteracao,\
                    qdg_Contingenciado,\
                    qdg_Cota,\
                    qdg_Bloqueado,\
                    qdg_DespesaAutorizada,\
                    qdg_Empenhado,\
                    qdg_Disponivel,\
                    qdg_Liquidado)\
                     values ("'+registro[0]+'",\
                    "'+registro[1]+'",\
                    "'+registro[2]+'",\
                    "'+registro[3]+'",\
                    "'+registro[4]+'",\
                    "'+registro[5]+'",\
                    "'+registro[6]+'",\
                    "'+registro[7]+'",\
                    "'+registro[8]+'",\
                    "'+registro[9]+'",\
                    "'+registro[10]+'",\
                    "'+registro[11]+'",\
                    "'+registro[12]+'",\
                    "'+registro[13]+'",\
                    "'+registro[14]+'",\
                    "'+registro[15]+'",\
                    "'+registro[16]+'",\
                    "'+registro[17]+'");')
       

        
        
        
        
 