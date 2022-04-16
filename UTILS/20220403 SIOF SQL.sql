-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SIOF
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SIOF
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SIOF` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema siof
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema siof
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `siof` DEFAULT CHARACTER SET utf8mb4 ;
USE `SIOF` ;

-- -----------------------------------------------------
-- Table `SIOF`.`tbl_ProcessoAquisicaoServico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_ProcessoAquisicaoServico` (
  `Id_ProcessoAquisicaoServico` VARCHAR(19) NOT NULL,
  `pas_Responsavel` VARCHAR(45) NULL,
  `pas_Descricao` VARCHAR(500) NULL,
  PRIMARY KEY (`Id_ProcessoAquisicaoServico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_PrevisaoFaseExecucao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_PrevisaoFaseExecucao` (
  `Id_PrevisaoFaseExecucao` INT NOT NULL,
  `fse_Fase` VARCHAR(45) NULL,
  `fse_Inicio` DATE NULL,
  `fse_Termino` DATE NULL,
  `fse_ProcessoAquisicaoServico` VARCHAR(19) NOT NULL,
  PRIMARY KEY (`Id_PrevisaoFaseExecucao`),
  INDEX `fk_tbl_PrevisaoFaseExecucao_tbl_ProcessoAquisicaoServico_idx` (`fse_ProcessoAquisicaoServico` ASC) ,
  CONSTRAINT `fk_tbl_PrevisaoFaseExecucao_tbl_ProcessoAquisicaoServico`
    FOREIGN KEY (`fse_ProcessoAquisicaoServico`)
    REFERENCES `SIOF`.`tbl_ProcessoAquisicaoServico` (`Id_ProcessoAquisicaoServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_objetivo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_objetivo` (
  `Id_Objetivo` INT NOT NULL AUTO_INCREMENT,
  `obj_Codigo` VARCHAR(3) NOT NULL,
  `obj_Descricao` VARCHAR(250) NOT NULL,
  `obj_Status` TINYINT(1) NULL DEFAULT '1',
  `obj_Observacao` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_Objetivo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_estrategia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_estrategia` (
  `Id_Estrategia` INT NOT NULL AUTO_INCREMENT,
  `est_Codigo` VARCHAR(6) NOT NULL,
  `est_Objetivo` INT NOT NULL,
  `est_Descricao` VARCHAR(250) NOT NULL,
  `est_Status` TINYINT(1) NULL DEFAULT '1',
  `est_Observacao` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_Estrategia`),
  INDEX `est_Objetio_Id_Objetivo_idx` (`est_Objetivo` ASC) ,
  CONSTRAINT `est_Objetivo_Id_Objetivo`
    FOREIGN KEY (`est_Objetivo`)
    REFERENCES `siof`.`tbl_objetivo` (`Id_Objetivo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_iniciativaestrategica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_iniciativaestrategica` (
  `Id_IniciativaEstrategica` INT NOT NULL AUTO_INCREMENT,
  `ini_Codigo` VARCHAR(9) NOT NULL,
  `ini_Estrategia` INT NOT NULL,
  `ini_Descricao` VARCHAR(250) NOT NULL,
  `ini_Status` TINYINT(1) NULL DEFAULT '1',
  `ini_Observacao` VARCHAR(1000) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_IniciativaEstrategica`),
  INDEX `ini_Estrategia_idx` (`ini_Estrategia` ASC) ,
  CONSTRAINT `ini_Estrategia_Id_Estrategia`
    FOREIGN KEY (`ini_Estrategia`)
    REFERENCES `siof`.`tbl_estrategia` (`Id_Estrategia`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_AlinhamentoEstrategico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_AlinhamentoEstrategico` (
  `Id_AlinhamentoEstrategico` INT NOT NULL,
  `ale_ProcessoAquisicaoServico` VARCHAR(19) NOT NULL,
  `ale_IniciativaEstrategica` INT NOT NULL,
  PRIMARY KEY (`Id_AlinhamentoEstrategico`),
  INDEX `fk_tbl_AlinhamentoEstrategico_tbl_ProcessoAquisicaoServico1_idx` (`ale_ProcessoAquisicaoServico` ASC) ,
  INDEX `fk_tbl_AlinhamentoEstrategico_tbl_iniciativaestrategica1_idx` (`ale_IniciativaEstrategica` ASC) ,
  CONSTRAINT `fk_tbl_AlinhamentoEstrategico_tbl_ProcessoAquisicaoServico1`
    FOREIGN KEY (`ale_ProcessoAquisicaoServico`)
    REFERENCES `SIOF`.`tbl_ProcessoAquisicaoServico` (`Id_ProcessoAquisicaoServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_AlinhamentoEstrategico_tbl_iniciativaestrategica1`
    FOREIGN KEY (`ale_IniciativaEstrategica`)
    REFERENCES `siof`.`tbl_iniciativaestrategica` (`Id_IniciativaEstrategica`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_coordenadoressetoriais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_coordenadoressetoriais` (
  `cso_Codigo` VARCHAR(8) NOT NULL,
  `cso_Nome` VARCHAR(255) NOT NULL,
  `cso_AreaTematica` VARCHAR(255) NULL DEFAULT NULL,
  `cso_DataInclusao` DATE NULL DEFAULT NULL,
  `cso_Status` TINYINT NULL DEFAULT NULL,
  `cso_InstrumentoLegal` VARCHAR(255) NULL DEFAULT NULL,
  `cso_OrdenadorDespesa` VARCHAR(11) NULL DEFAULT NULL,
  PRIMARY KEY (`cso_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_disponibilidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_disponibilidade` (
  `Id_Disponibilidade` INT NOT NULL AUTO_INCREMENT,
  `dsp_Status` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_Disponibilidade`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_especiedisponibilidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_especiedisponibilidade` (
  `Id_EspecieDisponibilidade` INT NOT NULL AUTO_INCREMENT,
  `esd_Disponibilidade` INT NOT NULL,
  `esd_Discriminacao` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Id_EspecieDisponibilidade`),
  INDEX `esd_Disponibilidade_Id_Disponibilidade_idx` (`esd_Disponibilidade` ASC) ,
  CONSTRAINT `esd_Disponibilidade_Id_Disponibilidade`
    FOREIGN KEY (`esd_Disponibilidade`)
    REFERENCES `siof`.`tbl_disponibilidade` (`Id_Disponibilidade`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfnaturezadespesadetalhada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfnaturezadespesadetalhada` (
  `nfc_Codigo` VARCHAR(8) NOT NULL,
  `nfc_Descricao` VARCHAR(255) NULL DEFAULT NULL,
  `nfc_CategoriaEconomica` VARCHAR(3) NULL DEFAULT NULL,
  `nfc_GrupoDespesa` VARCHAR(3) NULL DEFAULT NULL,
  `nfc_ModalidadeAplicacao` VARCHAR(3) NULL DEFAULT NULL,
  `nfc_ElementoDespesa` VARCHAR(3) NULL DEFAULT NULL,
  PRIMARY KEY (`nfc_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfnaturezadespesadetalhada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfnaturezadespesadetalhada` (
  `ndf_Codigo` VARCHAR(8) NOT NULL,
  `ndf_Descricao` VARCHAR(255) NOT NULL,
  `ndf_CategoriaEconomica` VARCHAR(3) NOT NULL,
  `ndf_GrupoDespesa` VARCHAR(3) NOT NULL,
  `ndf_ModalidadeAplicacao` VARCHAR(2) NOT NULL,
  `ndf_ElementoDespesa` VARCHAR(3) NULL DEFAULT NULL,
  PRIMARY KEY (`ndf_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_periodicidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_periodicidade` (
  `Id_Periodicidade` TINYINT(1) NOT NULL,
  `per_Descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_Periodicidade`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_produtounidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_produtounidade` (
  `pdu_Codigo` INT NOT NULL,
  `pdu_Especificacao` VARCHAR(45) NULL DEFAULT NULL,
  `pdu_UnidadeMedida` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`pdu_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_cadastrodemandas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_cadastrodemandas` (
  `Id_CadastroDemandas` INT NOT NULL AUTO_INCREMENT,
  `cad_CodigoDemanda` INT NOT NULL,
  `cad_CoordenadorSetorial` VARCHAR(8) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NOT NULL,
  `cad_Descricao` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `cad_FCDFDespesaDetalhada` VARCHAR(8) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `cad_GDFDespesaDetalhada` VARCHAR(8) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `cad_ProdutoUnidade` INT NULL DEFAULT NULL,
  `cad_Periodicidade` TINYINT(1) NULL DEFAULT NULL,
  `cad_EspecieDisponibilidade` INT NULL DEFAULT NULL,
  `cad_Observacao` VARCHAR(1000) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `cad_DataInclusao` DATE NULL DEFAULT NULL,
  `cad_Status` TINYINT NULL DEFAULT '1',
  `cad_EspecieDespesa` VARCHAR(2500) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  PRIMARY KEY (`Id_CadastroDemandas`),
  INDEX `cad_CoordenadorSetorial_cso_Codigo` (`cad_CoordenadorSetorial` ASC) ,
  INDEX `cad_FCDFNaurezaDespesaDetalhada_nfc_Codigo` (`cad_FCDFDespesaDetalhada` ASC) ,
  INDEX `cad_NaturezaDespesaDetalhada_nfc_Codigo` (`cad_GDFDespesaDetalhada` ASC) ,
  INDEX `cad_ProdutoUnidade_pdu_Codigo` (`cad_ProdutoUnidade` ASC) ,
  INDEX `cad_Periodicidade_Id_Periodicidade` (`cad_Periodicidade` ASC) ,
  INDEX `cad_EspecieDisponibilidade_Id_EspecieDisponibilidade_idx` (`cad_EspecieDisponibilidade` ASC) ,
  CONSTRAINT `cad_CoordenadorSetorial_cso_Codigo`
    FOREIGN KEY (`cad_CoordenadorSetorial`)
    REFERENCES `siof`.`tbl_coordenadoressetoriais` (`cso_Codigo`),
  CONSTRAINT `cad_EspecieDisponibilidade_Id_EspecieDisponibilidade`
    FOREIGN KEY (`cad_EspecieDisponibilidade`)
    REFERENCES `siof`.`tbl_especiedisponibilidade` (`Id_EspecieDisponibilidade`),
  CONSTRAINT `cad_FCDFFDespesaDetalhada_nfc_Codigo`
    FOREIGN KEY (`cad_FCDFDespesaDetalhada`)
    REFERENCES `siof`.`tbl_fcdfnaturezadespesadetalhada` (`nfc_Codigo`),
  CONSTRAINT `cad_GDFDespesaDetalhada_ndf_Codigo`
    FOREIGN KEY (`cad_GDFDespesaDetalhada`)
    REFERENCES `siof`.`tbl_gdfnaturezadespesadetalhada` (`ndf_Codigo`),
  CONSTRAINT `cad_Periodicidade_Id_Periodicidade`
    FOREIGN KEY (`cad_Periodicidade`)
    REFERENCES `siof`.`tbl_periodicidade` (`Id_Periodicidade`),
  CONSTRAINT `cad_ProdutoUnidade_pdu_Codigo`
    FOREIGN KEY (`cad_ProdutoUnidade`)
    REFERENCES `siof`.`tbl_produtounidade` (`pdu_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_ItemAquisicaoServico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_ItemAquisicaoServico` (
  `Id_ItemAqusicaoServico` INT NOT NULL,
  `ias_ProcessoAqusicaoServico` VARCHAR(19) NOT NULL,
  `ias_Codigo` INT NULL,
  `ias_Descricao` VARCHAR(500) NULL,
  `ias_Quantidade` INT NULL,
  `ias_UnidadeMedida` VARCHAR(45) NULL,
  `ias_Valor` DECIMAL(15,2) NULL,
  `ias_CadastroDemanda` INT NOT NULL,
  PRIMARY KEY (`Id_ItemAqusicaoServico`),
  INDEX `fk_tbl_ItemAquisicaoServico_tbl_cadastrodemandas1_idx` (`ias_CadastroDemanda` ASC) ,
  INDEX `fk_tbl_ItemAquisicaoServico_tbl_ProcessoAquisicaoServico1_idx` (`ias_ProcessoAqusicaoServico` ASC) ,
  CONSTRAINT `fk_tbl_ItemAquisicaoServico_tbl_cadastrodemandas1`
    FOREIGN KEY (`ias_CadastroDemanda`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_ItemAquisicaoServico_tbl_ProcessoAquisicaoServico1`
    FOREIGN KEY (`ias_ProcessoAqusicaoServico`)
    REFERENCES `SIOF`.`tbl_ProcessoAquisicaoServico` (`Id_ProcessoAquisicaoServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfplanointernoorcamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfplanointernoorcamento` (
  `Id_FCDFPlanoInterno` INT NOT NULL AUTO_INCREMENT,
  `pif_CadastroDemanda` INT NOT NULL,
  `pif_Justificativa` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `pif_UnidadeOrcamentaria` VARCHAR(6) NULL,
  `pif_Fonte` VARCHAR(3) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `pif_ProgramaTrabalho` VARCHAR(17) NULL,
  `pif_Quantidade` INT NULL DEFAULT NULL,
  `pif_Valor` DECIMAL(15,2) NULL DEFAULT NULL,
  `pif_Exercicio` YEAR NULL DEFAULT NULL,
  `pif_Observacao` VARCHAR(1000) NULL DEFAULT NULL,
  `pif_Data` DATE NOT NULL,
  PRIMARY KEY (`Id_FCDFPlanoInterno`),
  INDEX `fk_tbl_fcdfplanointernoorcamento_tbl_cadastrodemandas1_idx` (`pif_CadastroDemanda` ASC) ,
  CONSTRAINT `fk_tbl_fcdfplanointernoorcamento_tbl_cadastrodemandas1`
    FOREIGN KEY (`pif_CadastroDemanda`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfquadrodetalhamentodespesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfquadrodetalhamentodespesa` (
  `id_GDFQuadroDetalhamentoDespesa` INT NOT NULL AUTO_INCREMENT,
  `qdf_ExercícioFinanceiro` YEAR NULL DEFAULT NULL,
  `qdf_UnidadeOrcamentaria` INT NULL DEFAULT NULL,
  `qdf_MesReferencia` VARCHAR(11) CHARACTER SET 'latin1' NULL DEFAULT NULL,
  `qdf_DataEmissão` DATE NULL DEFAULT NULL,
  `qdf_Esfera` INT NULL DEFAULT NULL,
  `qdf_NaturezaDespesa` INT NULL DEFAULT NULL,
  `qdf_Fonte` INT NULL DEFAULT NULL,
  `qdf_ProgramaTrabalho` VARCHAR(17) NULL,
  `qdf_Lei` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Alteracao` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Contingenciado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Cota` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Bloqueado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_DespesaAutorizada` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Empenhado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Disponivel` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdf_Liquidado` DECIMAL(15,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_GDFQuadroDetalhamentoDespesa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_FCDFCreditosOrcamentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_FCDFCreditosOrcamentarios` (
  `Id_FCDFCreditosOrcamentarios` INT NOT NULL,
  `cof_FCDFPlanoInternoOrcamento` INT NOT NULL,
  `cof_FCDFQuadroDetalhamentoDespesa` INT NOT NULL,
  PRIMARY KEY (`Id_FCDFCreditosOrcamentarios`),
  INDEX `fk_table1_tbl_fcdfplanointernoorcamento1_idx` (`cof_FCDFPlanoInternoOrcamento` ASC) ,
  INDEX `fk_table1_tbl_fcdfquadrodetalhamentodespesa1_idx` (`cof_FCDFQuadroDetalhamentoDespesa` ASC) ,
  CONSTRAINT `fk_table1_tbl_fcdfplanointernoorcamento1`
    FOREIGN KEY (`cof_FCDFPlanoInternoOrcamento`)
    REFERENCES `siof`.`tbl_fcdfplanointernoorcamento` (`Id_FCDFPlanoInterno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_table1_tbl_fcdfquadrodetalhamentodespesa1`
    FOREIGN KEY (`cof_FCDFQuadroDetalhamentoDespesa`)
    REFERENCES `siof`.`tbl_fcdfquadrodetalhamentodespesa` (`id_GDFQuadroDetalhamentoDespesa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfplanointernoorcamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfplanointernoorcamento` (
  `Id_GDFPlanoInternoOrcamento` INT NOT NULL AUTO_INCREMENT,
  `pig_CadastroDemanda` INT NOT NULL,
  `pig_Quantidade` INT NULL DEFAULT NULL,
  `pig_Valor` DECIMAL(15,2) NULL DEFAULT NULL,
  `pig_Data` DATE NOT NULL,
  `pig_Observacoes` VARCHAR(1000) NULL,
  PRIMARY KEY (`Id_GDFPlanoInternoOrcamento`),
  INDEX `fk_tbl_gdfplanointernoorcamento_tbl_cadastrodemandas1_idx` (`pig_CadastroDemanda` ASC) ,
  CONSTRAINT `fk_tbl_gdfplanointernoorcamento_tbl_cadastrodemandas1`
    FOREIGN KEY (`pig_CadastroDemanda`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfquadrodetalhamentodespesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfquadrodetalhamentodespesa` (
  `id_GDFQuadroDetalhamentoDespesa` INT NOT NULL AUTO_INCREMENT,
  `qdg_ExercícioFinanceiro` YEAR NULL DEFAULT NULL,
  `qdg_UnidadeOrcamentaria` INT NULL DEFAULT NULL,
  `qdg_MesReferencia` VARCHAR(11) CHARACTER SET 'latin1' NULL DEFAULT NULL,
  `qdg_DataEmissão` DATE NULL DEFAULT NULL,
  `qdg_Esfera` INT NULL DEFAULT NULL,
  `qdg_NaturezaDespesa` INT NULL DEFAULT NULL,
  `qdg_Fonte` INT NULL DEFAULT NULL,
  `qdg_IdentificadorUso` INT NULL DEFAULT NULL,
  `qdg_ProgramaTrabalho` VARCHAR(17) NULL,
  `qdg_Lei` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Alteracao` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Contingenciado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Cota` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Bloqueado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_DespesaAutorizada` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Empenhado` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Disponivel` DECIMAL(15,2) NULL DEFAULT NULL,
  `qdg_Liquidado` DECIMAL(15,2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_GDFQuadroDetalhamentoDespesa`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_GDFPIOCreditosOrcamentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_GDFPIOCreditosOrcamentarios` (
  `Id_GDFPIOCreditosOrcamentarios` INT NOT NULL,
  `cog_GDFPlanoInternoOrcamento` INT NOT NULL,
  `cog_GDFQuadroDetalhamentoDespesa` INT NOT NULL,
  PRIMARY KEY (`Id_GDFPIOCreditosOrcamentarios`),
  INDEX `fk_tbl_GDFPIOCreditosOrcamentarios_tbl_gdfplanointernoorcam_idx` (`cog_GDFPlanoInternoOrcamento` ASC) ,
  INDEX `fk_tbl_GDFPIOCreditosOrcamentarios_tbl_gdfquadrodetalhament_idx` (`cog_GDFQuadroDetalhamentoDespesa` ASC) ,
  CONSTRAINT `fk_tbl_GDFPIOCreditosOrcamentarios_tbl_gdfplanointernoorcamen1`
    FOREIGN KEY (`cog_GDFPlanoInternoOrcamento`)
    REFERENCES `siof`.`tbl_gdfplanointernoorcamento` (`Id_GDFPlanoInternoOrcamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_GDFPIOCreditosOrcamentarios_tbl_gdfquadrodetalhamentod1`
    FOREIGN KEY (`cog_GDFQuadroDetalhamentoDespesa`)
    REFERENCES `siof`.`tbl_gdfquadrodetalhamentodespesa` (`id_GDFQuadroDetalhamentoDespesa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfempenho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfempenho` (
  `emf_Codigo` VARCHAR(23) NOT NULL,
  `emf_Descricao` VARCHAR(1000) NOT NULL,
  `emf_NumeroProcesso` VARCHAR(23) NULL DEFAULT NULL,
  `emf_DataEmissao` DATE NULL DEFAULT NULL,
  `emf_Esfera` VARCHAR(23) NULL DEFAULT NULL,
  `emf_Fonte` VARCHAR(10) NULL DEFAULT NULL,
  `emf_ProgramaTrabalhoResumido` VARCHAR(10) NULL DEFAULT NULL,
  PRIMARY KEY (`emf_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfitemempenho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfitemempenho` (
  `Id_FCDFItemEmpenho` INT NOT NULL AUTO_INCREMENT,
  `ias_ItemAquisicaoServico` INT NOT NULL,
  `itf_Empenho` VARCHAR(23) NOT NULL,
  `itf_Descricao` VARCHAR(100) NOT NULL,
  `itf_Operacao` VARCHAR(50) NOT NULL,
  `itf_Quantidade` DECIMAL(15,2) NULL DEFAULT NULL,
  `itf_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `itf_Data` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`Id_FCDFItemEmpenho`),
  INDEX `itf_Empenho_emf_Codigo_idx` (`itf_Empenho` ASC) ,
  INDEX `fk_tbl_fcdfitem_tbl_ItemAquisicaoServico1_idx` (`ias_ItemAquisicaoServico` ASC) ,
  CONSTRAINT `itf_Empenho_emf_Codigo`
    FOREIGN KEY (`itf_Empenho`)
    REFERENCES `siof`.`tbl_fcdfempenho` (`emf_Codigo`)
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tbl_fcdfitem_tbl_ItemAquisicaoServico1`
    FOREIGN KEY (`ias_ItemAquisicaoServico`)
    REFERENCES `SIOF`.`tbl_ItemAquisicaoServico` (`Id_ItemAqusicaoServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_fcdfitemliquidacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_fcdfitemliquidacao` (
  `Id_FCDFItemLiquidacao` INT NOT NULL,
  `lig_FCDFItemEmpenho` INT NOT NULL,
  `lig_Quantidade` DECIMAL(15,2) NULL,
  `lig_Valor` DECIMAL(15,2) NULL,
  PRIMARY KEY (`Id_FCDFItemLiquidacao`),
  INDEX `fk_tbl_fcdfitemliquidacao_tbl_fcdfitemempenho1_idx` (`lig_FCDFItemEmpenho` ASC) ,
  CONSTRAINT `fk_tbl_fcdfitemliquidacao_tbl_fcdfitemempenho1`
    FOREIGN KEY (`lig_FCDFItemEmpenho`)
    REFERENCES `siof`.`tbl_fcdfitemempenho` (`Id_FCDFItemEmpenho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_FCDFItemPagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_FCDFItemPagamento` (
  `Id_FCDFItemPagamento` INT NOT NULL,
  `pgf_FCDFItemLiquidacao` INT NOT NULL,
  `pgf_Quantidade` DECIMAL(15,2) NULL,
  `pgf_Vavlor` DECIMAL(15,2) NULL,
  `pgf_Data` DATE NULL,
  PRIMARY KEY (`Id_FCDFItemPagamento`),
  INDEX `fk_tbl_FCDFItemPagamento_tbl_fcdfitemliquidacao1_idx` (`pgf_FCDFItemLiquidacao` ASC) ,
  CONSTRAINT `fk_tbl_FCDFItemPagamento_tbl_fcdfitemliquidacao1`
    FOREIGN KEY (`pgf_FCDFItemLiquidacao`)
    REFERENCES `SIOF`.`tbl_fcdfitemliquidacao` (`Id_FCDFItemLiquidacao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfempenho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfempenho` (
  `emg_Codigo` VARCHAR(23) NOT NULL,
  `emg_Descricao` VARCHAR(1000) NOT NULL,
  `emf_NumeroProcesso` VARCHAR(23) NULL DEFAULT NULL,
  `emf_DataEmissao` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`emg_Codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfitemempenho`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfitemempenho` (
  `Id_GDFItemEmpenho` INT NOT NULL AUTO_INCREMENT,
  `ias_ItemAquisicaoServico` INT NOT NULL,
  `itf_Descricao` VARCHAR(100) NOT NULL,
  `itf_Operacao` VARCHAR(50) NOT NULL,
  `itf_Quantidade` DECIMAL(15,2) NULL DEFAULT NULL,
  `itg_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `itg_Data` DATE NULL DEFAULT NULL,
  `itg_GDFEmpenho` VARCHAR(23) NOT NULL,
  PRIMARY KEY (`Id_GDFItemEmpenho`),
  INDEX `fk_tbl_fcdfitem_tbl_ItemAquisicaoServico1_idx` (`ias_ItemAquisicaoServico` ASC) ,
  INDEX `fk_tbl_gdfitemempenho_tbl_gdfempenho1_idx` (`itg_GDFEmpenho` ASC) ,
  CONSTRAINT `fk_tbl_fcdfitem_tbl_ItemAquisicaoServico10`
    FOREIGN KEY (`ias_ItemAquisicaoServico`)
    REFERENCES `SIOF`.`tbl_ItemAquisicaoServico` (`Id_ItemAqusicaoServico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_gdfitemempenho_tbl_gdfempenho1`
    FOREIGN KEY (`itg_GDFEmpenho`)
    REFERENCES `siof`.`tbl_gdfempenho` (`emg_Codigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_GDFItemLiquidacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_GDFItemLiquidacao` (
  `Id_GDFItemLiquidacao` INT NOT NULL,
  `lig_GDFItemEmpenho` INT NOT NULL,
  `lig_Qantidade` DECIMAL(15,2) NULL,
  `lig_Valor` DECIMAL(15,2) NULL,
  PRIMARY KEY (`Id_GDFItemLiquidacao`),
  INDEX `fk_int_tbl_gdfitemempenho1_idx` (`lig_GDFItemEmpenho` ASC) ,
  CONSTRAINT `fk_int_tbl_gdfitemempenho1`
    FOREIGN KEY (`lig_GDFItemEmpenho`)
    REFERENCES `siof`.`tbl_gdfitemempenho` (`Id_GDFItemEmpenho`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SIOF`.`tbl_GDFItemPagamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SIOF`.`tbl_GDFItemPagamento` (
  `Id_GDFItemPagamento` INT NOT NULL,
  `pag_GDFItemLiquidacao` INT NOT NULL,
  `pag_Qantidade` DECIMAL(15,2) NULL,
  `pag_Valor` DECIMAL(15,2) NULL,
  PRIMARY KEY (`Id_GDFItemPagamento`),
  INDEX `fk_tbl_GDFItemLiquidacao_copy1_tbl_GDFItemLiquidacao1_idx` (`pag_GDFItemLiquidacao` ASC) ,
  CONSTRAINT `fk_tbl_GDFItemLiquidacao_copy1_tbl_GDFItemLiquidacao1`
    FOREIGN KEY (`pag_GDFItemLiquidacao`)
    REFERENCES `SIOF`.`tbl_GDFItemLiquidacao` (`Id_GDFItemLiquidacao`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `siof` ;

-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfproposta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfproposta` (
  `Id_FCDFProposta` INT NOT NULL AUTO_INCREMENT,
  `prf_CadastroDemanda` INT NOT NULL,
  `prf_Justificativa` VARCHAR(255) NULL DEFAULT NULL,
  `prf_Quantidade` INT NULL DEFAULT '0',
  `prf_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `prf_Fonte` VARCHAR(3) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `prf_ProgramaTrabalho` VARCHAR(45) NULL,
  `prf_Exercicio` YEAR NULL DEFAULT NULL,
  PRIMARY KEY (`Id_FCDFProposta`),
  INDEX `fk_tbl_fcdfproposta_tbl_cadastrodemandas1_idx` (`prf_CadastroDemanda` ASC) ,
  CONSTRAINT `fk_tbl_fcdfproposta_tbl_cadastrodemandas1`
    FOREIGN KEY (`prf_CadastroDemanda`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_fcdfremanejamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_fcdfremanejamento` (
  `Id_FCDFRemanejamentos` INT NOT NULL AUTO_INCREMENT,
  `ref_PlanoInterno` INT NOT NULL,
  `ref_Descricao` VARCHAR(1000) NULL DEFAULT NULL,
  `ref_EspecieRemanejamento` ENUM('Cancelamento', 'Suplementação') CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NOT NULL,
  `ref_Quantidade` INT NULL DEFAULT '1',
  `ref_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `ref_Data` DATE NOT NULL,
  PRIMARY KEY (`Id_FCDFRemanejamentos`),
  INDEX `fk_tbl_fcdfremanejamento_tbl_fcdfplanointernoorcamento1_idx` (`ref_PlanoInterno` ASC) ,
  CONSTRAINT `fk_tbl_fcdfremanejamento_tbl_fcdfplanointernoorcamento1`
    FOREIGN KEY (`ref_PlanoInterno`)
    REFERENCES `siof`.`tbl_fcdfplanointernoorcamento` (`Id_FCDFPlanoInterno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfproposta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfproposta` (
  `Id_GDFProposta` INT NOT NULL AUTO_INCREMENT,
  `prg_CadastroDemada` INT NOT NULL,
  `prg_Justificativa` VARCHAR(255) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `prg_Quantidade` INT NULL DEFAULT '0',
  `prg_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `prg_UnidadeOrcamentaria` VARCHAR(5) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `prg_Fonte` VARCHAR(9) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NULL DEFAULT NULL,
  `prg_IdentificadorUso` INT NULL DEFAULT NULL,
  `prg_ProgramaTrabalho` VARCHAR(17) NULL,
  `prg_Exercicio` YEAR NULL DEFAULT NULL,
  PRIMARY KEY (`Id_GDFProposta`),
  INDEX `fk_tbl_gdfproposta_tbl_cadastrodemandas1_idx` (`prg_CadastroDemada` ASC) ,
  CONSTRAINT `fk_tbl_gdfproposta_tbl_cadastrodemandas1`
    FOREIGN KEY (`prg_CadastroDemada`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_gdfremanejamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_gdfremanejamento` (
  `Id_GDFRemanejamentos` INT NOT NULL AUTO_INCREMENT,
  `reg_Descricao` VARCHAR(1000) NULL DEFAULT NULL,
  `reg_EspecieRemanejamento` ENUM('Cancelamento', 'Suplementação') CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci' NOT NULL,
  `reg_Quantidade` INT NULL DEFAULT '1',
  `reg_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `reg_Data` DATE NOT NULL,
  `reg_PlanoInterno` INT NOT NULL,
  PRIMARY KEY (`Id_GDFRemanejamentos`),
  INDEX `fk_tbl_gdfremanejamento_tbl_gdfplanointernoorcamento1_idx` (`reg_PlanoInterno` ASC) ,
  CONSTRAINT `fk_tbl_gdfremanejamento_tbl_gdfplanointernoorcamento1`
    FOREIGN KEY (`reg_PlanoInterno`)
    REFERENCES `siof`.`tbl_gdfplanointernoorcamento` (`Id_GDFPlanoInternoOrcamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


-- -----------------------------------------------------
-- Table `siof`.`tbl_propostasetorial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `siof`.`tbl_propostasetorial` (
  `Id_PropostaSetorial` INT NOT NULL AUTO_INCREMENT,
  `pps_CadastroDemanda` INT NOT NULL,
  `pps_Justificativa` VARCHAR(255) NULL DEFAULT NULL,
  `pps_Quantidade` INT NULL DEFAULT '1',
  `pps_Valor` DECIMAL(15,2) NULL DEFAULT '0.00',
  `pps_Observacao` VARCHAR(1000) NULL DEFAULT NULL,
  `pps_UnidadeDemandante` VARCHAR(255) NULL DEFAULT NULL,
  `pps_Exercicio` YEAR NOT NULL,
  `pps_Status` TINYINT(1) NULL DEFAULT '1',
  `pps_Data` DATE NOT NULL,
  PRIMARY KEY (`Id_PropostaSetorial`),
  INDEX `pps_CadastroDemanda_Id_CadastroDemandas` (`pps_CadastroDemanda` ASC) ,
  CONSTRAINT `pps_CadastroDemanda_Id_CadastroDemandas`
    FOREIGN KEY (`pps_CadastroDemanda`)
    REFERENCES `siof`.`tbl_cadastrodemandas` (`Id_CadastroDemandas`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_general_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
