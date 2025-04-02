--  tabela de operadoras
CREATE TABLE operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    UF VARCHAR(2),
    CEP VARCHAR(10),
    DDD VARCHAR(3),
    Telefone VARCHAR(15),
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE
);

-- tabela financeira
CREATE TABLE financeiro (
    DATA DATE,
    REG_ANS INT,
    CD_CONTA_CONTABIL VARCHAR(20),
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
);


-- Importar dados das operadoras
LOAD DATA INFILE '3-test-sql-finan\\Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Registro_ANS, @CNPJ, @Razao_Social, @Nome_Fantasia, @Modalidade, @Logradouro, @Numero, @Complemento, @Bairro, @Cidade, @UF, @CEP, @DDD, @Telefone, @Fax, @Endereco_eletronico, @Representante, @Cargo_Representante, @Regiao_de_Comercializacao, @Data_Registro_ANS)
SET Data_Registro_ANS = STR_TO_DATE(@Data_Registro_ANS, '%Y-%m-%d');

-- Import dos dados financeiros

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\1T2023.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\2T2023.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\3T2023.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\4T2023.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\1T2024.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\2T2024.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\3T2024.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE '3-test-sql-finan\\financeiros\\4T2024.csv'
INTO TABLE financeiro
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


--  10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR" no último trimestre
SELECT f.REG_ANS, o.Razao_Social, SUM(f.VL_SALDO_FINAL) AS Total_Despesas
FROM financeiro f
JOIN operadoras o ON f.REG_ANS = o.Registro_ANS
WHERE f.DESCRICAO LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR%'
AND f.DATA >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY f.REG_ANS, o.Razao_Social
ORDER BY Total_Despesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas nessa categoria no último ano
SELECT f.REG_ANS, o.Razao_Social, SUM(f.VL_SALDO_FINAL) AS Total_Despesas
FROM financeiro f
JOIN operadoras o ON f.REG_ANS = o.Registro_ANS
WHERE f.DESCRICAO LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR%'
AND f.DATA >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY f.REG_ANS, o.Razao_Social
ORDER BY Total_Despesas DESC
LIMIT 10;
