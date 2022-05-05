import csv
import re
import datetime

def importarQDD (nomeTabela):
    tbl_QDDGDF = open(nomeTabela, encoding = 'latin-1')
    QDDGDF_Readeble = csv.reader(tbl_QDDGDF, delimiter=';')
    QDDGDF = list(QDDGDF_Readeble)
    return QDDGDF



lista = importarQDD('24103.csv')



UO = re.sub('Unidade Orçamentária: ','', lista[2][0])
mesReferencia = re.sub('Mês de Referência: ', '', lista[3][0])
emissao = re.search(r'\d{2}/\d{2}/\d{4}', lista[4][0]).group()
dataEmissao = datetime.datetime.strptime(emissao, "%d/%m/%Y").strftime("%Y-%m-%d")


for linha in lista:
    esfera = re.search('\d\d\d\d\d\d',linha[0])
    if re.search('\d\d\d\d\d\d',linha[0]):
 