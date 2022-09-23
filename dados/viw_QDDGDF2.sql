use siof;
create view viw_qddGDF as 
SELECT qdg_ExercicioFinanceiro as "Exercicio", qdg_MesReferencia as "Mes", qdg_DataEmissao as "Emissao",
	case 
	when qdg_UnidadeOrcamentaria = 24904 then "Departamento de Logística e Finanças"
    when qdg_UnidadeOrcamentaria = 24901 then "Departamento de Saúde"
    when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '06.122.8217.8502.8765' then "Departamento de Gestão de Pessoal"
	when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '06.122.8217.8504.9584' then "Departamento de Gestão de Pessoal"
	when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '09.272.0001.9004.0009' then "Departamento de Gestão de Pessoal"
            else "Departamento de Logística e Finanças"
            end as `Departamento`,
	case
	when qdg_Fonte = 100000000 and qdg_IdentificadorUso = 0 then "GDF"
    when qdg_Fonte = 100000000 and qdg_IdentificadorUso = 6 then "Emenda Distrital"
    when qdg_Fonte = 117000000 and qdg_IdentificadorUso = 0 then "FunPM"
    when qdg_Fonte = 121000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 131000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 132000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 171000000 and qdg_IdentificadorUso = 0 then "FunPM"
    when qdg_Fonte = 183000000 and qdg_IdentificadorUso = 4 then "Convênios"
    when qdg_Fonte = 183000000 and qdg_IdentificadorUso = 0 then "GDF"
    when qdg_Fonte = 317000000 and qdg_IdentificadorUso = 0 then "FunPM"
    when qdg_Fonte = 320000000 and qdg_IdentificadorUso = 0 then "FunPM"
    when qdg_Fonte = 321000000 and qdg_IdentificadorUso = 4 then "Convênios"
    when qdg_Fonte = 321000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 331000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 332000000 and qdg_IdentificadorUso = 0 then "Convênios"
    when qdg_Fonte = 371000000 and qdg_IdentificadorUso = 0 then "FunPM"
    when qdg_Fonte = 390000000 and qdg_IdentificadorUso = 4 then "GDF"
    when qdg_Fonte = 721000000 and qdg_IdentificadorUso = 0 then "GDF"
    when qdg_Fonte = 732000000 and qdg_IdentificadorUso = 0 then "Emenda Federal"
    when qdg_Fonte = 821000000 and qdg_IdentificadorUso = 0 then "Emenda Federal"
    end as `Fonte`,
	case 
    when  substr(qdg_NaturezaDespesa, 2, 1) = 1 then "Pessoal e encargos sociais"
    when  substr(qdg_NaturezaDespesa, 2, 1) = 3 then "Outras despesas correntes"
	when  substr(qdg_NaturezaDespesa, 2, 1) = 4 then "Investimentos"
    end as "Grupo",
    qdg_Lei as "Lei", qdg_Alteracao as "Altarecao", qdg_DespesaAutorizada as "Autorizada", qdg_Empenhado as "Empenhado", qdg_Liquidado as "Liquidado"
    FROM siof.tbl_gdfquadrodetalhamentodespesa;