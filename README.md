# 💐 Projeto de Governança, Qualidade e Limpeza de Dados - Floricultura

Repositório desenvolvido com foco em **Governança de Dados**, **Data Quality** e **Padronização de Processos**, simulando um cenário real de tratamento de bases de dados desestruturadas no segmento de comércio varejista de flores.

---

## 🎯 Objetivo do Projeto
Demonstrar a aplicação prática de técnicas de engenharia e governança de dados — desde a concepção do dicionário técnico até a automação da limpeza de registros em **Python (Pandas)**, garantindo a integridade, consistência e confiabilidade das informações de vendas.

---

## 📂 Estrutura do Repositório

```text
governanca-dados-floricultura/
│
├── dados_brutos/
│   └── dados_brutos_flores.csv    # Base original contendo inconsistências e erros proposituais.
│
├── dados_tratados/
│   └── dados_tratados_flores.csv  # Base final limpa, auditada e padronizada.
│
├── documentacao/
│   └── dicionario_de_dados.md     # Especificação técnica das colunas e regras de negócio.
│
└── scripts/
    └── limpeza_dados.py           # Script automatizado de tratamento em Python (Pandas).
```

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- Python & Pandas (Tratamento, manipulação e automação de dados)

- Markdown (Documentação estruturada)

- Git & GitHub (Controle de versão e portfólio)

---

## 🔍 Problemas Identificados na Base Bruta

Durante a auditoria inicial da base de vendas, foram mapeadas as seguintes inconsistências:

- **Nomes de Clientes:** Variações de preenchimento (nomes completos, abreviações como "J. Paes" e textos em letras minúsculas).

- **Datas:** Conflito entre o formato brasileiro (`DD/MM/YYYY`) e o internacional (`YYYY-MM-DD`).

- **Atributos Categóricos:** Grafias divergentes e misturas de termos por extenso com abreviações (ex: `Grande` vs `G`, `Delivery` vs `delivery`).

- **Formatação de Preços:** Presença de símbolos monetários (`R$`) e vírgulas misturados com formatos decimais em ponto.

- **Status do Pedido:** Valores com variações de caixa (`Concluido`, `concluído`, `Entregue`) e campos totalmente vazios (`NaN`).

---

## 💡 Aprendizados e Evolução

Este projeto permitiu consolidar conceitos fundamentais de governança através de:

- **Padronização de Domínios:** Criação de regras restritas para categorias como tamanhos de buquê, tipos de entrega e status de pedidos.

- **Resiliência em Scripts:** Tratamento avançado de exceções e conversões utilizando parâmetros do Pandas (`errors='coerce'`, `format='mixed'`, `dayfirst=True`).

- **Visão Analítica:** Transformação de dados brutos e caóticos em uma fonte de dados pronta para auditoria e tomada de decisão estratégica no negócio.

--- 

## 👩‍💻 Autora

Bianca Inazumi
