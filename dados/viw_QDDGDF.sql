SELECT case 
	when qdg_UnidadeOrcamentaria = 24904 then "Departamento de Logística e Finanças"
    when qdg_UnidadeOrcamentaria = 24901 then "Departamento de Saúde"
    when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '06.122.8217.8502.8765' then "Departamento de Gestão de Pessoal"
	when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '06.122.8217.8504.9584' then "Departamento de Gestão de Pessoal"
	when qdg_UnidadeOrcamentaria = 24103 and qdg_ProgramaTrabalho = '09.272.0001.9004.0009' then "Departamento de Gestão de Pessoal"
            else "Departamento de Logística e Finanças"
            end as `Departamento`,
	case 
    when  substr(qdg_NaturezaDespesa, 2, 1) = 1 then "Pessoal e encargos sociais"
    when  substr(qdg_NaturezaDespesa, 2, 1) = 3 then "Outras despesas correntes"
	when  substr(qdg_NaturezaDespesa, 2, 1) = 4 then "Investimentos"
    end as "Grupo de Despesa"
    
    FROM siof.tbl_gdfquadrodetalhamentodespesa;