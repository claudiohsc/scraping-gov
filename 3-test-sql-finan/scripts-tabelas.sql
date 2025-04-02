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
