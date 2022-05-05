use siof;
CREATE VIEW viw_QDDFCDF AS SELECT qdf_DataEmissao as Emissão,
qdf_ExercicioFinanceiro as Ano,
if(left(qdf_Acao, 4) = "00FM", "Departamento de Saúde",
if(left(qdf_Acao, 4) = "00Q2", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00NS", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00NT", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00RS", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00NR" and left(qdf_NaturezaDespesa, 2) = "31", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00NR" and left(qdf_NaturezaDespesa, 6) = "339015", "Departamento de Gestão de Pessoal",
if(left(qdf_Acao, 4) = "00NR" and left(qdf_NaturezaDespesa, 6) = "339019", "Departamento de Gestão de Pessoal",
"Departamento de Logística e Finanças")))))))) as `Ordenador de Despesa`,
CONCAT(left(qdf_Funcao,2), ".", left(qdf_Subfuncao, 3), ".", left(qdf_Programa, 4), ".", left(qdf_Acao, 4), ".", left(qdf_Subtitulo,4)) as `Programa de Trabalho`,
MID(qdf_PlanoOrcamentario, 7),
if(left(qdf_NaturezaDespesa, 2) = 31, "Pessoal", if(left(qdf_NaturezaDespesa, 2) = 33, "Outras Despesas Correntes", "Investimento")) as `Grupo de Despesa`,
SUM(qdf_Lei) as Lei,
SUM(qdf_DotacaoInicial) as `Dotacao Inicial`,
SUM(qdf_DotacaoAtual) as `Dotação Atual`,
SUM(qdf_Empenhado) as `Empenhado`,
SUM(qdf_Liquidado) as `Liquidado`,
SUM(qdf_Pago) as `Pago`
 FROM siof.tbl_fcdfquadrodetalhamentodespesa
 WHERE left(qdf_PlanoOrcamentario, 4) like "0002" or left(qdf_PlanoOrcamentario, 4) = "0005" or left(qdf_PlanoOrcamentario, 4) = "0009"
 GROUP BY Emissão, Ano, `Ordenador de Despesa`, `Programa de Trabalho`, `Grupo de Despesa`;