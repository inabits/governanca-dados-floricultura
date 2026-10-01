# Dicionário de Dados - Projeto Floricultura 💐

Este documento descreve a estrutura técnica e as regras de negócio de cada campo presente na base de dados de vendas de buquês.

## Tabela: `dados_brutos_cafe.csv`

| Coluna | Tipo de Dado | Obrigatório? (Sim/Não) | Regra de Negócio / Padrão Esperado |
| :--- | :--- | :--- | :--- |
| **id_venda** | Inteiro (INT) | Sim | Identificador único e sequencial de cada venda realizada. Não pode se repetir ou ser nulo. |
| **cliente** | Texto (String) | Sim | Nome completo do cliente. Deve ser padronizado sem abreviações e sem erros de digitação (Ex: "Juliana Paes", e não "J. Paes"). |
| **data_transacao** | Data (YYYY-MM-DD) | Sim | Data em que a transação foi efetuada. O formato oficial padrão aceito é o internacional `AAAA-MM-DD`. |
| **nome_flor** | Texto (String) | Sim | Nome da flor do buquê. |
| **tamanho_buque** | Texto (String) | Sim | Indica o tamanho do buquê. Valores permitidos: `Grande`, `Médio` e `Pequeno`. |
| **tipo_entrega** | Texto (String) | Sim | Indica o tipo de entrega que foi realizado. Valores permitidos: `Retirada` e `Delivery`. |
| **preco_total** | Numérico (Float) | Sim | Valor monetário total pago pelo pedido. Deve conter apenas números e ponto decimal (Ex: `35.00`), sem o símbolo de moeda. |
| **status_pedido**| Texto (String) | Sim | Situação atual do pedido. Valores permitidos: `Concluído`, `Pendente`, `Entregue` ou `Cancelado`. |