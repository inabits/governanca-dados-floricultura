import pandas as pd

# CARREGAR DADOS BRUTOS
df = pd.read_csv('dados_brutos/dados_brutos_flores.csv')

# PADRONIZAÇÃO DE NOMES DE CLIENTES
df['cliente'] = df['cliente'].fillna('Desconhecido')
df['cliente'] = df['cliente'].replace({'J. Paes': 'Juliana Paes'})
df['cliente'] = df['cliente'].str.strip().str.title()

# PADRONIZAÇÃO DE DATAS
df['data_transacao'] = pd.to_datetime(df['data_transacao'], dayfirst=True, format='mixed', errors='coerce')

# PADRONIZAÇÃO DE NOME DE FLOR
df['nome_flor'] = df['nome_flor'].replace({'Orquidea Phalaenopsis': 'Orquídea Phalaenopsis'})
df['nome_flor'] = df['nome_flor'].replace({'Buquê Tulipas Holandesas': 'Tulipas Holandesas'})
df['nome_flor'] = df['nome_flor'].str.strip().str.title()

# PADRONIZAÇÃO DE TAMANHO DE BUQUÊ
df['tamanho_buque'] = df['tamanho_buque'].str.strip().str.lower()
mapa_tamanho = {
    'grande': 'Grande',
    'g': 'Grande',
    'médio': 'Médio',
    'medio': 'Médio',
    'pequeno': 'Pequeno',
    'p': 'Pequeno'
}
df['tamanho_buque'] = df['tamanho_buque'].map(mapa_tamanho)

# PADRONIZAÇÃO DE TIPO DE ENTREGA
df['tipo_entrega'] = df['tipo_entrega'].str.strip().str.title()

# PADRONIZAÇÃO DE PREÇO
df['preco_total'] = df['preco_total'].astype(str).str.replace('R$', '')
df['preco_total'] = df['preco_total'].str.replace(',', '.')
df['preco_total'] = pd.to_numeric(df['preco_total'], errors='coerce')

# PADRONIZAÇÃO DO STATUS DO PEDIDO
df['status_pedido'] = df['status_pedido'].fillna('Pendente')
df['status_pedido'] = df['status_pedido'].str.replace('Concluido', 'Concluído')
df['status_pedido'] = df['status_pedido'].str.strip().str.title()

# SALVAR DADOS LIMPOS
df.to_csv('dados_tratados/dados_tratados_flores.csv', index=False)